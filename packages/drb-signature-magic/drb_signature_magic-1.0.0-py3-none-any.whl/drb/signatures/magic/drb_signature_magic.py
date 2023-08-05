from enum import Enum
from drb.core.node import DrbNode
from drb.core.signature import Signature
from drb.signatures.magic.execptions import DrbSignatureMagicException
import io
import re


class MagicType(Enum):
    bytes = 1
    string = 2
    regex = 3
    hexa = 4


class MagicSignature(Signature):
    """
    Allowing to check if a DRB Node match a Magic signature.
    """
    def __init__(self, list_args: dict):
        self.__offset = list_args.get('offset', 0)
        self.__pattern = list_args.get('pattern')
        if self.__pattern is None or len(self.__pattern) == 0:
            raise DrbSignatureMagicException('Magic signature '
                                             'incorrect definition '
                                             'pattern is not defined '
                                             f': {str(list_args)}')
        type = list_args.get('type', 'string')

        type = type.lower()

        if type == MagicType.hexa.name:
            self.__type = MagicType.hexa
            if not isinstance(self.__pattern, bytes):
                self.__pattern = bytearray.fromhex(self.__pattern)
        if type == MagicType.bytes.name:
            self.__type = MagicType.bytes
            if not isinstance(self.__pattern, bytes):
                self.__pattern = self.__pattern.encode()
        elif type == MagicType.regex.name:
            self.__type = MagicType.regex

            if not isinstance(self.__pattern, str):
                if isinstance(self.__pattern, bytes):
                    self.__pattern = self.__pattern.decode()
                else:
                    self.__pattern = str(self.__pattern)
        elif type == MagicType.string.name:
            self.__type = MagicType.string

            if not isinstance(self.__pattern, str):
                if isinstance(self.__pattern, bytes):
                    self.__pattern = self.__pattern.decode()
                else:
                    self.__pattern = str(self.__pattern)

    def matches(self, node: DrbNode) -> bool:
        try:
            stream_io = node.get_impl(io.BufferedIOBase)
            return self.check_signature(stream_io)
        except Exception as Error:
            return False

    def to_dict(self) -> dict:
        data = {'pattern': self.__pattern, 'type': self.__type.name}

        if self.__offset is not None:
            data['offset'] = self.__offset
        return data

    @staticmethod
    def get_name():
        return 'magic'

    def check_signature(self, stream_io: io.BufferedIOBase):
        self.skip_offset(stream_io)

        if self.__type == MagicType.bytes or self.__type == MagicType.hexa:
            buff = stream_io.read(len(self.__pattern))
            if buff == self.__pattern:
                return True
        elif self.__type == MagicType.string:
            buff = stream_io.read(len(self.__pattern.encode()))
            str_read = buff.decode()
            if str_read == self.__pattern:
                return True
        elif self.__type == MagicType.regex:
            buff = stream_io.read(255)

            str_read = buff.decode()
            if re.match(self.__pattern, str_read):
                return True
        return False

    def skip_offset(self, stream_io: io.BufferedIOBase):
        if stream_io.seekable():
            stream_io.seek(self.__offset)
        else:
            stream_io.read(self.__offset)
