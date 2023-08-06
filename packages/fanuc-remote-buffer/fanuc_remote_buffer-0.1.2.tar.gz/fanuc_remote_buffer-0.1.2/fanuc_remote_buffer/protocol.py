from binascii import hexlify, unhexlify
from construct import Struct, Const, Byte, Bytes, Adapter, Default, PaddedString, Switch, If, RawCopy, Checksum, Tell, Pointer, Padding, Enum, Computed, ExprAdapter

TODO = Bytes(1)

Command_desc = {
    "SYN": "Initialization command (R/H)",
    "RDY": "Notice of initialization end (R/H)",
    "RST": "Notice of CNC reset (R)",
    "ARS": "Response corresponding to the RST (H)",
    "ALM": "Notice of CNC alarm occurrence (R)",
    "AAL": "Response corresponding to the ALM (H)",
    "SAT": "Notice of remote buffer status (R)",
    "SET": "Response corresponding to the SAT (H)",
    "GTD": "Transmit command of NC data (R)",
    "DAT": "Response corresponding to the GTD (H)",
    "WAT": "Response corresponding to the GTD (H)",
    "EOD": "Response corresponding to GTD (H)",
    "CLB": "Buffer clear (H)",
    "RDI": "DI reading request (H)",
    "SDI": "Notice of DI (R)",
    "SDO": "Do output request (H)",
    "RTY": "Request of retransmission (R/H)",
}

Hex_Nibble = ExprAdapter(
    PaddedString(1, 'ascii'),
    lambda obj, ctx: int(obj, 16),
    lambda obj, ctx: "%01X" % obj,
)

Hex_Byte = ExprAdapter(
    PaddedString(2, 'ascii'),
    lambda obj, ctx: int(obj, 16),
    lambda obj, ctx: "%02X" % obj,
)

Hex_Word = ExprAdapter(
    PaddedString(4, 'ascii'),
    lambda obj, ctx: int(obj, 16),
    lambda obj, ctx: "%04X" % obj,
)

Command_SAT = Struct(
    "b1" / Hex_Nibble,
    "b2" / Hex_Nibble,
    "b3" / Hex_Nibble,
    "b4" / Hex_Nibble,
    "b5" / Hex_Word,
    "b9" / Hex_Word,
    "b13" / Hex_Word,
    "b17" / Hex_Word,
    "b21" / Hex_Word,
    "b25" / Hex_Word,
    "b29" / Hex_Word,
    "b33" / Hex_Word,
    "b37" / Hex_Word,
    "b41" / Hex_Word,
    "b45" / Hex_Byte,
    "b47" / Hex_Byte,
    "b49" / Padding(5),
    "b55" / Hex_Byte,
)

Commands = {
    "SAT": Bytes(56), # TODO: Command_SAT
    "SET": Bytes(56), # TODO: Command_SET
    "GTD": TODO,
    "DAT": TODO,
    "RDI": TODO,
    "SDI": Hex_Byte,
    "SDO": Hex_Byte,
    "RTY": Hex_Nibble,
}

Commands_with_data = (
    "SAT",
    "SET",
    "GTD",
    "DAT",
    "RDI",
    "SDI",
    "SDO",
    "RTY",
)

def protocol_a_checksum(data):
    s = 0
    for c in data:
        s += c
    return "%02X" % (s % 0xFF)

import enum
class Commands_enum(enum.Enum):
    SYN = "SYN"
    RDY = "RDY"
    RST = "RST"
    ARS = "ARS"
    ALM = "ALM"
    AAL = "AAL"
    SAT = "SAT"
    SET = "SET"
    GTD = "GTD"
    DAT = "DAT"
    WAT = "WAT"
    EOD = "EOD"
    CLB = "CLB"
    RDI = "RDI"
    SDI = "SDI"
    SDO = "SDO"
    RTY = "RTY"


Protocol_A = Struct(
    "offset" / Tell,
    "checksum" / Padding(2),
    "fields" / RawCopy(Struct(
        "command" / Enum(PaddedString(3, "ascii"), Commands_enum) * "Command",
        "data" / If(
            lambda ctx: ctx.command in Commands_with_data,
            Switch(lambda ctx: ctx.command, Commands)
        ) * "Data",
        Const(3, Byte) * "ETX",
    )),
    "checksum" / Pointer(lambda ctx:ctx.offset, Checksum(PaddedString(2, 'ascii'),
        lambda data: protocol_a_checksum(data),
        lambda ctx: ctx.fields.data )),
    "command" / Computed(lambda ctx: ctx.fields.value.command),
    "data" / Computed(lambda ctx: ctx.fields.value.data),
)

