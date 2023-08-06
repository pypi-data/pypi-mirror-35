from construct import Byte, Bytes, Checksum, Computed, Const, Enum, \
    ExprAdapter, If, PaddedString, Padding, Pointer, RawCopy, Struct, Switch, \
    Tell
import enum

"""
fanuc_remote_buffer.protocol

"""

TODO = Bytes(1)


class Protocol:
    """handle protocol structures for fanuc remote buffer

    This class stores configuration and
    generates construct structures based on the configuration.

    :Example:
    >>> from fanuc_remote_buffer.protocol import Protocol
    >>> P = Protocol().get_protocol_a()
    >>> pkt = P.parse(b'08SYN\\r')
    >>> "%s" % pkt.command
    SYN
    """

    def __init__(self):
        self.ETX = 0x0D  #: ETX character for the packets

    #: Brief descriptions from the official documentation
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

    #: ExprAdapter for a single hex digit
    Hex_Nibble = ExprAdapter(
        PaddedString(1, 'ascii'),
        lambda obj, ctx: int(obj, 16),
        lambda obj, ctx: "%01X" % obj,
    )

    #: ExprAdapter for a single byte in hex
    Hex_Byte = ExprAdapter(
        PaddedString(2, 'ascii'),
        lambda obj, ctx: int(obj, 16),
        lambda obj, ctx: "%02X" % obj,
    )

    #: ExprAdapter for a single word in hex
    Hex_Word = ExprAdapter(
        PaddedString(4, 'ascii'),
        lambda obj, ctx: int(obj, 16),
        lambda obj, ctx: "%04X" % obj,
    )

    #: Structure for SAT: remote buffer status
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

    #: Commands linked to specific structures
    Commands = {
        "SAT": Bytes(56),  # TODO: Implement Command_SAT
        "SET": Bytes(56),  # TODO: Implement Command_SET
        "GTD": TODO,
        "DAT": TODO,
        "RDI": TODO,
        "SDI": Hex_Byte,
        "SDO": Hex_Byte,
        "RTY": Hex_Nibble,
    }

    #: Commands that have a data field
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

    @staticmethod
    def protocol_a_checksum(data):
        """calculate a checksum for given data

        Checksum for protocol A is a binary sum of the rest of the packet

        :param data: input data
        :type data: bytes
        :returns: checksum as a hex string
        :rtype: str
        """
        s = 0
        for c in data:
            s += c
        return "%02X" % (s % 0xFF)

    #: List of available commands
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

    def get_protocol_a(self):
        """returns a protocol A structure

        generates a construct Struct based on current settings

        :returns: Protocol A structure
        :rtype: construct.Struct
        """

        Protocol_A = Struct(
            "offset" / Tell,
            "checksum" / Padding(2),
            "fields" / RawCopy(Struct(
                "command" / Enum(
                    PaddedString(3, "ascii"),
                    self.Commands_enum
                ) * "Command",
                "data" / If(
                    lambda ctx: ctx.command in self.Commands_with_data,
                    Switch(lambda ctx: ctx.command, self.Commands)
                ) * "Data",
                Const(self.ETX, Byte) * "ETX",
            )),
            "checksum" / Pointer(lambda ctx: ctx.offset, Checksum(
                PaddedString(2, 'ascii'),
                lambda data: self.protocol_a_checksum(data),
                lambda ctx: ctx.fields.data)
            ),
            "command" / Computed(lambda ctx: ctx.fields.value.command),
            "data" / Computed(lambda ctx: ctx.fields.value.data),
        )

        return Protocol_A
