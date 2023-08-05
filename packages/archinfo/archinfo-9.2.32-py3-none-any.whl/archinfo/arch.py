import logging
from typing import Dict, List, Tuple
import struct as _struct
import platform as _platform
import re

from .archerror import ArchError
from . import RegisterOffset, RegisterName
from .tls import TLSArchInfo

import copy

l = logging.getLogger("archinfo.arch")
l.addHandler(logging.NullHandler())

try:
    import pyvex as _pyvex
except ImportError:
    _pyvex = None

try:
    import unicorn as _unicorn
except ImportError:
    _unicorn = None

try:
    import capstone as _capstone
except ImportError:
    _capstone = None

try:
    import keystone as _keystone
except ImportError:
    _keystone = None


class Endness: # pylint: disable=no-init
    """ Endness specifies the byte order for integer values

    :cvar LE:      little endian, least significant byte is stored at lowest address
    :cvar BE:      big endian, most significant byte is stored at lowest address
    :cvar ME:      Middle-endian. Yep.
    """
    LE = "Iend_LE"
    BE = "Iend_BE"
    ME = 'Iend_ME'


class Register:
    """
    A collection of information about a register. Each different architecture
    has its own list of registers, which is the base for all other
    register-related collections.

    It is, just like for Arch object, assumed that the information is compatible
    with PyVEX.

    :ivar str  name: The name of the register
    :ivar int  size: The size of the register (in bytes)
    :ivar int  vex_offset: The VEX offset used to identify this register
    :ivar str  vex_name: The name libVEX uses to identify the register
    :ivar list subregisters: The list of subregisters in the form (name, offset from vex_offset, size)
    :ivar tuple alias_names: The list of possible alias names
    :ivar bool general_purpose: Whether this is a general purpose register
    :ivar bool floating_point: Whether this is a floating-point register
    :ivar bool vector: Whether this is a vector register
    :ivar bool argument: Whether this is an argument register
    :ivar bool persistent: Whether this is a persistent register
    :ivar tuple default_value: The offset of the instruction pointer in the register file
    :ivar int, str linux_entry_value: The offset of the instruction pointer in the register file
    :ivar bool concretize_unique: Whether this register should be concretized, if unique, at the end of each block
    :ivar bool concrete: Whether this register should be considered during the synchronization of the concrete execution
                         of the process
    :ivar bool artificial: Whether this register is an artificial register added by VEX IR or other ILs.
    """
    def __init__(self, name, size, vex_offset=None, vex_name=None, subregisters=None,
                 alias_names=None, general_purpose=False, floating_point=False,
                 vector=False, argument=False, persistent=False, default_value=None,
                 linux_entry_value=None, concretize_unique=False, concrete=True,
                 artificial=False):
        self.name = name # type: RegisterName
        self.size = size # type: int
        self.vex_offset = vex_offset # type: RegisterOffset
        self.vex_name = vex_name
        self.subregisters = [] if subregisters is None else subregisters # type: List[Tuple[RegisterName, RegisterOffset, int]]
        self.alias_names = () if alias_names is None else alias_names
        self.general_purpose = general_purpose
        self.floating_point = floating_point
        self.vector = vector
        self.argument= argument
        self.persistent = persistent
        self.default_value = default_value
        self.linux_entry_value = linux_entry_value
        self.concretize_unique = concretize_unique
        self.concrete = concrete
        self.artificial = artificial

    def __repr__(self):
        return f'<Register {self.name}>'

class Arch:
    """
    A collection of information about a given architecture. This class should be subclasses for each different
    architecture, and then that subclass should be registered with the ``register_arch`` method.

    A good number of assumptions are made that code is being processed under the VEX IR - for instance, it is expected
    the register file offsets are expected to match code generated by PyVEX.

    Arches may be compared with == and !=.

    :ivar str name: The name of the arch
    :ivar int bits: The number of bits in a word
    :ivar str vex_arch: The VEX enum name used to identify this arch
    :ivar str qemu_name: The name used by QEMU to identify this arch
    :ivar str ida_processor: The processor string used by IDA to identify this arch
    :ivar str triplet: The triplet used to identify a linux system on this arch
    :ivar int max_inst_bytes: The maximum number of bytes in a single instruction
    :ivar int ip_offset: The offset of the instruction pointer in the register file
    :ivar int sp_offset: The offset of the stack pointer in the register file
    :ivar int bp_offset: The offset of the base pointer in the register file
    :ivar int lr_offset: The offset of the link register (return address) in the register file
    :ivar int ret_offset: The offset of the return value register in the register file
    :ivar bool vex_conditional_helpers: Whether libVEX will generate code to process the conditional flags for this
            arch using ccalls
    :ivar int syscall_num_offset: The offset in the register file where the syscall number is stored
    :ivar bool call_pushes_ret: Whether this arch's call instruction causes a stack push
    :ivar int stack_change: The change to the stack pointer caused by a push instruction
    :ivar str memory_endness: The endness of memory, as a VEX enum
    :ivar str register_endness: The endness of registers, as a VEX enum. Should usually be same as above
    :ivar str instruction_endness: The endness of instructions stored in memory.
        In other words, this controls whether instructions are stored endian-flipped compared to their description
        in the ISA manual, and should be flipped when lifted. Iend_BE means "don't flip"
        NOTE: Only used for non-libVEX lifters.
    :ivar dict sizeof: A mapping from C type to variable size in bits
    :ivar cs_arch: The Capstone arch value for this arch
    :ivar cs_mode: The Capstone mode value for this arch
    :ivar ks_arch: The Keystone arch value for this arch
    :ivar ks_mode: The Keystone mode value for this arch
    :ivar uc_arch: The Unicorn engine arch value for this arch
    :ivar uc_mode: The Unicorn engine mode value for this arch
    :ivar uc_const: The Unicorn engine constants module for this arch
    :ivar uc_prefix: The prefix used for variables in the Unicorn engine constants module
    :ivar list function_prologs: A list of regular expressions matching the bytes for common function prologues
    :ivar list function_epilogs: A list of regular expressions matching the bytes for common function epilogues
    :ivar str ret_instruction: The bytes for a return instruction
    :ivar str nop_instruction: The bytes for a nop instruction
    :ivar int instruction_alignment: The instruction alignment requirement
    :ivar list default_register_values: A weird listing describing how registers should be initialized for purposes of
            sanity
    :ivar dict entry_register_values: A mapping from register name to a description of the value that should be in it
            at program entry on linux
    :ivar list default_symbolic_register: Honestly, who knows what this is supposed to do. Fill it with the names of
            the general purpose registers.
    :ivar dict register_names: A mapping from register file offset to register name
    :ivar dict registers: A mapping from register name to a tuple of (register file offset, size in bytes)
    :ivar list lib_paths: A listing of common locations where shared libraries for this architecture may be found
    :ivar str got_section_name: The name of the GOT section in ELFs
    :ivar str ld_linux_name: The name of the linux dynamic loader program
    :cvar int byte_width: the number of bits in a byte.
    :ivar TLSArchInfo elf_tls: A description of how thread-local storage works
    """
    byte_width = 8
    instruction_endness = "Iend_BE"
    elf_tls = None  # type: TLSArchInfo

    def __init__(self, endness, instruction_endness=None):

        self.bytes = self.bits // self.byte_width

        if endness not in (Endness.LE, Endness.BE, Endness.ME):
            raise ArchError('Must pass a valid endness: Endness.LE, Endness.BE, or Endness.ME')

        if instruction_endness is not None:
            self.instruction_endness = instruction_endness

        if self.vex_support and _pyvex:
            self.vex_archinfo = _pyvex.default_vex_archinfo()

        if endness == Endness.BE:
            if self.vex_archinfo:
                self.vex_archinfo['endness'] = _pyvex.vex_endness_from_string('VexEndnessBE')
            self.memory_endness = Endness.BE
            self.register_endness = Endness.BE
            if _capstone and self.cs_mode is not None:
                self.cs_mode -= _capstone.CS_MODE_LITTLE_ENDIAN
                self.cs_mode += _capstone.CS_MODE_BIG_ENDIAN
            if _keystone and self.ks_mode is not None:
                self.ks_mode -= _keystone.KS_MODE_LITTLE_ENDIAN
                self.ks_mode += _keystone.KS_MODE_BIG_ENDIAN
            self.ret_instruction = reverse_ends(self.ret_instruction)
            self.nop_instruction = reverse_ends(self.nop_instruction)

        if self.register_list and _pyvex is not None:
            (_, _), max_offset = max(_pyvex.vex_ffi.guest_offsets.items(), key=lambda x: x[1])
            max_offset += self.bits
            # Register collections
            if type(self.vex_arch) is str:
                va = self.vex_arch[7:].lower() # pylint: disable=unsubscriptable-object
                for r in self.register_list:
                    if r.vex_offset is None:
                        for name in (r.vex_name, r.name) + r.alias_names:
                            try:
                                r.vex_offset = _pyvex.vex_ffi.guest_offsets[(va, name)]
                            except KeyError:
                                r.vex_offset = max_offset
                                max_offset += r.size
                            else:
                                break

            self.default_register_values = [(r.name,) + r.default_value for r in self.register_list if r.default_value is not None]
            self.entry_register_values = {r.name: r.linux_entry_value for r in self.register_list if r.linux_entry_value is not None}
            self.default_symbolic_registers = [r.name for r in self.register_list if r.general_purpose]
            self.register_names = {r.vex_offset: r.name for r in self.register_list}
            self.registers = self._get_register_dict()
            self.argument_registers = {r.vex_offset for r in self.register_list if r.argument}
            self.persistent_regs = [r.name for r in self.register_list if r.persistent]
            self.concretize_unique_registers = {r.vex_offset for r in self.register_list if r.concretize_unique}
            self.artificial_registers = {r.name for r in self.register_list if r.artificial}
            self.cpu_flag_register_offsets_and_bitmasks_map = {}
            self.reg_blacklist = []
            self.reg_blacklist_offsets = []

            # Artificial registers offsets
            self.artificial_registers_offsets = []
            for reg_name in self.artificial_registers:
                reg = self.get_register_by_name(reg_name)
                self.artificial_registers_offsets.extend(range(reg.vex_offset, reg.vex_offset + reg.size))

            # Register offsets
            try:
                self.ip_offset = self.registers['ip'][0]
                self.sp_offset = self.registers['sp'][0]
                self.bp_offset = self.registers['bp'][0]
                self.lr_offset = self.registers.get('lr', (None, None))[0]
            except KeyError:
                pass

        # generate register mapping (offset, size): name
        self.register_size_names = {}
        for reg in self.register_list:
            if reg.vex_offset is None:
                continue
            self.register_size_names[(reg.vex_offset, reg.size)] = reg.name
            for name, off, sz in reg.subregisters:
                # special hacks for X86 and AMD64 - don't translate register names to bp, sp, etc.
                if self.name in {'X86', 'AMD64'} and name in {'bp', 'sp', 'ip'}:
                    continue
                self.register_size_names[(reg.vex_offset + off, sz)] = name

        # allow mapping a sub-register to its base register
        self.subregister_map = { }
        for reg in self.register_list:
            if reg.vex_offset is None:
                continue
            base_reg = reg.vex_offset, reg.size
            self.subregister_map[(reg.vex_offset, reg.size)] = base_reg
            self.subregister_map[reg.vex_offset] = base_reg
            for name, off, sz in reg.subregisters:
                if self.name in {'X86', 'AMD64'} and name in {'bp', 'sp', 'ip'}:
                    continue
                subreg_offset = reg.vex_offset + off
                self.subregister_map[(subreg_offset, sz)] = base_reg
                if subreg_offset not in self.subregister_map:
                    self.subregister_map[subreg_offset] = base_reg

        # Unicorn specific stuff
        if self.uc_mode is not None:
            if endness == Endness.BE:
                self.uc_mode -= _unicorn.UC_MODE_LITTLE_ENDIAN
                self.uc_mode += _unicorn.UC_MODE_BIG_ENDIAN
            self.uc_regs = { }
            # map register names to Unicorn const
            for r in self.register_names.values():
                reg_name = self.uc_prefix + 'REG_' + r.upper()
                if hasattr(self.uc_const, reg_name):
                    self.uc_regs[r] = getattr(self.uc_const, reg_name)

            # VEX register offset to unicorn register ID map
            self.vex_to_unicorn_map = {}
            pc_reg_name = self.get_register_by_name("pc")
            for reg_name, unicorn_reg_id in self.uc_regs.items():
                if reg_name == pc_reg_name:
                    continue

                vex_reg = self.get_register_by_name(reg_name)
                self.vex_to_unicorn_map[vex_reg.vex_offset] = (unicorn_reg_id, vex_reg.size)

            # VEX registers used in lieu of flags register
            self.vex_cc_regs = []
            vex_cc_register_names = ["cc_op", "cc_dep1", "cc_dep2", "cc_ndep"]
            for reg_name in vex_cc_register_names:
                vex_flag_reg = self.get_register_by_name(reg_name)
                if vex_flag_reg is not None:
                    self.vex_cc_regs.append(vex_flag_reg)

    def copy(self):
        """
        Produce a copy of this instance of this arch.
        """
        res = copy.copy(self)
        res.vex_archinfo = copy.deepcopy(self.vex_archinfo)
        res._cs = None
        res._ks = None
        return res

    def __repr__(self):
        return f'<Arch {self.name} ({self.memory_endness[-2:]})>'

    def __hash__(self):
        return hash((self.name, self.bits, self.memory_endness))

    def __eq__(self, other):
        if not isinstance(other, Arch):
            return False
        return  self.name == other.name and \
                self.bits == other.bits and \
                self.memory_endness == other.memory_endness

    def __ne__(self, other):
        return not self == other

    def __getstate__(self):
        self._cs = None
        self._ks = None
        if self.vex_archinfo is not None:
            # clear hwcacheinfo-caches because it may contain cffi.CData
            self.vex_archinfo['hwcache_info']['caches'] = None
        return self.__dict__

    def __setstate__(self, data):
        self.__dict__.update(data)

    def get_register_by_name(self, reg_name):
        """
        Return the Register object associated with the given name.
        This includes subregisters.

        For example, if you are operating in a platform-independent
        setting, and wish to address "whatever the stack pointer is"
        you could pass 'sp' here, and get Register(...r13...) back
        on an ARM platform.
        """
        for r in self.register_list:
            if reg_name == r.name or reg_name in r.alias_names:
                return r
        return None

    def get_default_reg_value(self, register):
        if register == 'sp':
            # Convert it to the corresponding register name
            registers = [r for r, v in self.registers.items() if v[0] == self.sp_offset]
            if len(registers) > 0:
                register = registers[0]
            else:
                return None
        for reg, val, _, _ in self.default_register_values:
            if reg == register:
                return val
        return None

    def struct_fmt(self, size=None, signed=False, endness=None):
        """
        Produce a format string for use in python's ``struct`` module to decode a single word.

        :param int size:    The size in bytes to pack/unpack. Defaults to wordsize
        :param bool signed: Whether the data should be extracted signed/unsigned. Default unsigned
        :param str endness: The endian to use in packing/unpacking. Defaults to memory endness
        :return str:        A format string with an endness modifier and a single format character
        """
        if size is None:
            size = self.bytes
        if endness is None:
            endness = self.memory_endness

        if endness == Endness.BE:
            fmt_end = ">"
        elif endness == Endness.LE:
            fmt_end = "<"
        elif endness == Endness.ME:
            raise ValueError("Please don't middle-endian at me, I'm begging you")
        else:
            raise ValueError("Invalid endness value: %r" % endness)

        if size == 8:
            fmt_size = "Q"
        elif size == 4:
            fmt_size = "I"
        elif size == 2:
            fmt_size = "H"
        elif size == 1:
            fmt_size = "B"
        else:
            raise ValueError("Invalid size: Must be a integer power of 2 less than 16")

        if signed:
            fmt_size = fmt_size.lower()

        return fmt_end + fmt_size

    def _get_register_dict(self) -> Dict[RegisterName, Tuple[RegisterOffset, int]]:
        res = {}
        for r in self.register_list:
            if r.vex_offset is None:
                continue
            res[r.name] = (r.vex_offset, r.size)
            for i in r.alias_names:
                res[i] = (r.vex_offset, r.size)
            for reg, offset, size in r.subregisters:
                res[reg] = (r.vex_offset + offset, size)
        return res

    # e.g. sizeof['int'] = 32
    sizeof = {}

    @property
    def capstone(self):
        """
        A Capstone instance for this arch
        """
        if _capstone is None:
            raise Exception("Capstone is not installed!")
        if self.cs_arch is None:
            raise ArchError("Arch %s does not support disassembly with Capstone" % self.name)
        if self._cs is None:
            self._cs = _capstone.Cs(self.cs_arch, self.cs_mode)
            self._configure_capstone()
            self._cs.detail = True
        return self._cs

    @property
    def keystone(self):
        """
        A Keystone instance for this arch
        """
        if self._ks is None:
            if _keystone is None:
                raise Exception("Keystone is not installed!")
            if self.ks_arch is None:
                raise ArchError("Arch %s does not support disassembly with Keystone" % self.name)
            self._ks = _keystone.Ks(self.ks_arch, self.ks_mode)
            self._configure_keystone()
        return self._ks

    def _configure_capstone(self):
        pass

    def _configure_keystone(self):
        pass

    @property
    def unicorn(self):
        """
        A Unicorn engine instance for this arch
        """
        if _unicorn is None or self.uc_arch is None:
            raise ArchError("Arch %s does not support with Unicorn" % self.name)
        # always create a new Unicorn instance
        return _unicorn.Uc(self.uc_arch, self.uc_mode)

    def asm(self, string, addr=0, as_bytes=True, thumb=False):
        """
        Compile the assembly instruction represented by string using Keystone

        :param string:      The textual assembly instructions, separated by semicolons
        :param addr:        The address at which the text should be assembled, to deal with PC-relative access. Default 0
        :param as_bytes:    Set to False to return a list of integers instead of a python byte string
        :param thumb:       If working with an ARM processor, set to True to assemble in thumb mode.
        :return:            The assembled bytecode
        """
        if thumb and not hasattr(self, 'keystone_thumb'):
            l.warning("Specified thumb=True on non-ARM architecture")
            thumb = False
        ks = self.keystone_thumb if thumb else self.keystone # pylint: disable=no-member

        try:
            encoding, _ = ks.asm(string, addr, as_bytes) # pylint: disable=too-many-function-args
        except TypeError:
            bytelist, _ = ks.asm(string, addr)
            if as_bytes:
                if bytes is str:
                    encoding = ''.join(chr(c) for c in bytelist)
                else:
                    encoding = bytes(bytelist)
            else:
                encoding = bytelist

        return encoding

    def disasm(self, bytestring, addr=0, thumb=False):
        if thumb and not hasattr(self, 'capstone_thumb'):
            l.warning("Specified thumb=True on non-ARM architecture")
            thumb = False
        cs = self.capstone_thumb if thumb else self.capstone # pylint: disable=no-member
        return '\n'.join(f'{insn.address:#x}:\t{insn.mnemonic} {insn.op_str}' for insn in cs.disasm(bytestring, addr))

    def translate_dynamic_tag(self, tag):
        try:
            return self.dynamic_tag_translation[tag]
        except KeyError:
            if isinstance(tag, int):
                l.error("Please look up and add dynamic tag type %#x for %s", tag, self.name)
            return tag

    def translate_symbol_type(self, tag):
        try:
            return self.symbol_type_translation[tag]
        except KeyError:
            if isinstance(tag, int):
                l.error("Please look up and add symbol type %#x for %s", tag, self.name)
            return tag

    def translate_register_name(self, offset, size=None):
        if size is not None:
            try:
                return self.register_size_names[(offset, size)]
            except KeyError:
                pass

        try:
            return self.register_names[offset]
        except KeyError:
            return str(offset)

    def get_base_register(self, offset, size=None):
        """
        Convert a register or sub-register to its base register's offset.

        :param int offset:  The offset of the register to look up for.
        :param int size:    Size of the register.
        :return:            Offset and size of the base register, or None if no base register is found.
        """

        if size is None:
            key = offset
        else:
            key = (offset, size)

        return self.subregister_map.get(key, None)

    def get_register_offset(self, name):
        try:
            return self.registers[name][0]
        except:
            raise ValueError("Register %s does not exist!" % name)

    def is_artificial_register(self, offset, size):

        r = self.get_base_register(offset, size)
        if r is None:
            return False
        r_offset, _ = r

        try:
            r_name = self.register_names[r_offset]
        except KeyError:
            return False

        return r_name in self.artificial_registers

    # Determined by watching the output of strace ld-linux.so.2 --list --inhibit-cache
    def library_search_path(self, pedantic=False):
        """
        A list of paths in which to search for shared libraries.
        """
        subfunc = lambda x: x.replace('${TRIPLET}', self.triplet).replace('${ARCH}', self.linux_name)
        path = ['/lib/${TRIPLET}/', '/usr/lib/${TRIPLET}/', '/lib/', '/usr/lib', '/usr/${TRIPLET}/lib/']
        if self.bits == 64:
            path.append('/usr/${TRIPLET}/lib64/')
            path.append('/usr/lib64/')
            path.append('/lib64/')
        elif self.bits == 32:
            path.append('/usr/${TRIPLET}/lib32/')
            path.append('/usr/lib32/')
            path.append('/lib32/')

        if pedantic:
            path = sum([[x + 'tls/${ARCH}/', x + 'tls/', x + '${ARCH}/', x] for x in path], [])
        return list(map(subfunc, path))

    def m_addr(self, addr, *args, **kwargs):
        """
        Given the address of some code block, convert it to the address where this block
        is stored in memory. The memory address can also be referred to as the "real" address.

        :param addr:    The address to convert.
        :return:        The "real" address in memory.
        :rtype:         int
        """
        return addr

    def x_addr(self, addr, *args, **kwargs):
        """
        Given the address of some code block, convert it to the value that should be assigned
        to the instruction pointer register in order to execute the code in that block.

        :param addr:    The address to convert.
        :return:        The "execution" address.
        :rtype:         int
        """
        return addr

    def is_thumb(self, addr):  # pylint:disable=unused-argument
        """
        Return True, if the address is the THUMB address. False otherwise.

        For non-ARM architectures this method always returns False.

        :param addr:    The address to check.
        :return:        Whether the given address is the THUMB address.
        """
        return False

    @property
    def vex_support(self):
        """
        Whether the architecture is supported by VEX or not.

        :return: True if this Arch is supported by VEX, False otherwise.
        :rtype:  bool
        """

        return self.vex_arch is not None

    @property
    def unicorn_support(self):
        """
        Whether the architecture is supported by Unicorn engine or not,

        :return: True if this Arch is supported by the Unicorn engine, False otherwise.
        :rtype:  bool
        """

        return self.qemu_name is not None

    @property
    def capstone_support(self):
        """
        Whether the architecture is supported by the Capstone engine or not.

        :return: True if this Arch is supported by the Capstone engine, False otherwise.
        :rtype:  bool
        """

        return self.cs_arch is not None

    @property
    def keystone_support(self):
        """
        Whether the architecture is supported by the Keystone engine or not.

        :return: True if this Arch is supported by the Keystone engine, False otherwise.
        :rtype:  bool
        """

        return self.ks_arch is not None

    address_types = (int,)
    function_address_types = (int,)

    # various names
    name = None # type: str
    vex_arch = None
    qemu_name = None
    ida_processor = None
    linux_name = None
    triplet = None

    # instruction stuff
    max_inst_bytes = None
    ret_instruction = b''
    nop_instruction = b''
    instruction_alignment = None

    # register offsets
    ip_offset = None # type: RegisterOffset
    sp_offset = None # type: RegisterOffset
    bp_offset = None # type: RegisterOffset
    ret_offset = None # type: RegisterOffset
    fp_ret_offset = None # type: RegisterOffset
    lr_offset = None # type: RegisterOffset

    # whether or not VEX has ccall handlers for conditionals for this arch
    vex_conditional_helpers = False

    # memory stuff
    bits = None
    memory_endness = Endness.LE
    register_endness = Endness.LE
    stack_change = None

    # is it safe to cache IRSBs?
    cache_irsb = True

    branch_delay_slot = False

    function_prologs = set()
    function_epilogs = set()

    # Capstone stuff
    cs_arch = None
    cs_mode = None
    _cs = None

    # Keystone stuff
    ks_arch = None
    ks_mode = None
    _ks = None

    # Unicorn stuff
    uc_arch = None
    uc_mode = None
    uc_const = None
    uc_prefix = None
    uc_regs = None
    artificial_registers_offsets = None
    artificial_registers = None
    cpu_flag_register_offsets_and_bitmasks_map = None
    reg_blacklist = None
    reg_blacklist_offsets = None
    vex_to_unicorn_map = None
    vex_cc_regs = None

    call_pushes_ret = False
    initial_sp = 0x7fff0000

    # Difference of the stack pointer after a call instruction (or its equivalent) is executed
    call_sp_fix = 0

    stack_size = 0x8000000

    # Register information
    register_list = [] # type: List[Register]
    default_register_values = []
    entry_register_values = {}
    default_symbolic_registers = []
    registers = {} # type:  Dict[RegisterName, Tuple[RegisterOffset, int]]
    register_names = {} # type: Dict[RegisterOffset, RegisterName]
    argument_registers = set()
    argument_register_positions = {}
    persistent_regs = []
    concretize_unique_registers = set() # this is a list of registers that should be concretized, if unique, at the end of each block

    lib_paths = []
    reloc_s_a = []
    reloc_b_a = []
    reloc_s = []
    reloc_copy = []
    reloc_tls_mod_id = []
    reloc_tls_doffset = []
    reloc_tls_offset = []
    dynamic_tag_translation = {}
    symbol_type_translation = {}
    got_section_name = ''

    vex_archinfo = None


arch_id_map = []

all_arches = []


def register_arch(regexes, bits, endness, my_arch):
    """
    Register a new architecture.
    Architectures are loaded by their string name using ``arch_from_id()``, and
    this defines the mapping it uses to figure it out.
    Takes a list of regular expressions, and an Arch class as input.

    :param regexes: List of regular expressions (str or SRE_Pattern)
    :type regexes: list
    :param bits: The canonical "bits" of this architecture, ex. 32 or 64
    :type bits: int
    :param endness: The "endness" of this architecture.  Use Endness.LE, Endness.BE, Endness.ME, "any", or None if the
                    architecture has no intrinsic endianness.
    :type endness: str or None
    :param class my_arch:
    :return: None
    """
    if not isinstance(regexes, list):
        raise TypeError("regexes must be a list")
    for rx in regexes:
        if not isinstance(rx, str) and not isinstance(rx,re._pattern_type):
            raise TypeError("Each regex must be a string or compiled regular expression")
        try:
            re.compile(rx)
        except:
            raise ValueError('Invalid Regular Expression %s' % rx)
    #if not isinstance(my_arch,Arch):
    #    raise TypeError("Arch must be a subclass of archinfo.Arch")
    if not isinstance(bits, int):
        raise TypeError("Bits must be an int")
    if endness is not None:
        if endness not in (Endness.BE, Endness.LE, Endness.ME, 'any'):
            raise TypeError("Endness must be Endness.BE, Endness.LE, or 'any'")
    arch_id_map.append((regexes, bits, endness, my_arch))
    if endness == 'any':
        all_arches.append(my_arch(Endness.BE))
        all_arches.append(my_arch(Endness.LE))
    else:
        all_arches.append(my_arch(endness))


class ArchNotFound(Exception):
    pass


def arch_from_id(ident, endness='any', bits='') -> Arch:
    """
    Take our best guess at the arch referred to by the given identifier, and return an instance of its class.

    You may optionally provide the ``endness`` and ``bits`` parameters (strings) to help this function out.
    """
    if bits == 64 or (isinstance(bits, str) and '64' in bits):
        bits = 64
    elif isinstance(bits,str) and '32' in bits:
        bits = 32
    elif not bits and '64' in ident:
        bits = 64
    elif not bits and '32' in ident:
        bits = 32

    endness = endness.lower()
    if 'lit' in endness:
        endness = Endness.LE
    elif 'big' in endness:
        endness = Endness.BE
    elif 'lsb' in endness:
        endness = Endness.LE
    elif 'msb' in endness:
        endness = Endness.BE
    elif 'le' in endness:
        endness = Endness.LE
    elif 'be' in endness:
        endness = Endness.BE
    elif 'l' in endness:
        endness = 'unsure'
    elif 'b' in endness:
        endness = 'unsure'
    else:
        endness = 'unsure'
    ident = ident.lower()
    cls = None
    aendness = ""
    for arxs, abits, aendness, acls in arch_id_map:
        found_it = False
        for rx in arxs:
            if re.search(rx, ident):
                found_it = True
                break
        if not found_it:
            continue
        if bits and bits != abits:
            continue
        if aendness == 'any' or endness == aendness or endness == 'unsure':
            cls = acls
            break
    if not cls:
        raise ArchNotFound(f"Can't find architecture info for architecture {ident} with {repr(bits)} bits and {endness} endness")
    if endness == 'unsure':
        if aendness == 'any':
            # We really don't care, use default
            return cls()
        else:
            # We're expecting the ident to pick the endness.
            # ex. 'armeb' means obviously this is Iend_BE
            return cls(aendness)
    else:
        return cls(endness)


def reverse_ends(string):
    count = (len(string) + 3) // 4
    ise = 'I' * count
    string += b'\x00' * (count * 4 - len(string))
    return _struct.pack('>' + ise, *_struct.unpack('<' + ise, string))


def get_host_arch():
    """
    Return the arch of the machine we are currently running on.
    """
    return arch_from_id(_platform.machine())
