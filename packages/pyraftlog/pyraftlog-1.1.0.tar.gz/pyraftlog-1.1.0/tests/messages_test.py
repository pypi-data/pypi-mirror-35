import pytest

from pyraftlog.messages import Message


def test_message_serialisation():
    message = Message(Message.APPEND_ENTRIES, 'sender', 'recipient', 1, {})
    serialised = message.serialise()

    assert type(serialised) == str

    unserialised = Message.unserialise(serialised)

    assert type(unserialised) == Message
    assert unserialised.type == message.type
    assert unserialised.sender == message.sender
    assert unserialised.recipient == message.recipient
    assert unserialised.term == message.term
    assert unserialised.data == message.data
