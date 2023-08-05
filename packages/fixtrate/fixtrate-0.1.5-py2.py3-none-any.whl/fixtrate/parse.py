import simplefix
from . import message as fm


def _convert(msg, uid=None):
    new_msg = fm.FixMessage(uid)
    new_msg.begin_string = msg.begin_string
    new_msg.message_type = msg.message_type
    new_msg.pairs = msg.pairs
    new_msg.header_index = msg.header_index
    return new_msg


class FixParser(simplefix.FixParser):

    def get_message(self, uid=None):
        msg = super().get_message()
        # return msg
        if msg is None:
            return
        return _convert(msg, uid)

    @classmethod
    def parse(cls, raw_message, base=False):
        parser = cls()
        parser.append_buffer(raw_message)
        base_msg = parser.get_message()

        if base:
            return base_msg

        return _convert(base_msg)
