import redis
import pytest

from pyraftlog.boards import RedisBoard
from pyraftlog.boards import MemoryBoard
from pyraftlog.messages import Message


def test_memory_board_put_get_single_message():
    message_board = MemoryBoard()
    assert message_board.len('recipient') == 0
    assert message_board.len('sender') == 0

    posted = Message(Message.APPEND_ENTRIES, 'sender', 'recipient', 1, {})
    message_board.put(posted)

    assert message_board.len('recipient') == 1
    assert message_board.len('sender') == 0

    assert message_board.get('sender') is None
    received = message_board.get('recipient')

    assert type(received) == Message
    assert posted.term == received.term
    assert posted.data == received.data


def test_memory_board_message_length_and_order():
    message_board = MemoryBoard()
    assert message_board.len('recipient') == 0

    # Push messages to the board
    for x in range(1, 10):
        message_board.put(Message(Message.APPEND_ENTRIES, 'sender', 'recipient', 1, {"ord": x}))
        assert message_board.len('recipient') == 1

    # Pop the message from board asserting order
    message = message_board.get('recipient')
    assert message.data['ord'] == 9


def test_redis_board_put_get_single_message():
    message_board = RedisBoard(redis.Redis('localhost'))
    assert message_board.len('recipient') == 0
    assert message_board.len('sender') == 0

    posted = Message(Message.APPEND_ENTRIES, 'sender', 'recipient', 1, {})
    message_board.put(posted)

    assert message_board.len('recipient') == 1
    assert message_board.len('sender') == 0

    assert message_board.get('sender') is None
    received = message_board.get('recipient')

    assert type(received) == Message
    assert posted.term == received.term
    assert posted.data == received.data


def test_redis_board_message_length_and_order():
    message_board = RedisBoard(redis.Redis('localhost'))
    assert message_board.len('recipient') == 0

    # Push messages to the board
    for x in range(1, 10):
        message_board.put(Message(Message.APPEND_ENTRIES, 'sender', 'recipient', 1, {"ord": x}))
        assert message_board.len('recipient') == 1

    # Pop the message from board asserting order
    message = message_board.get('recipient')
    assert message.data['ord'] == 9
