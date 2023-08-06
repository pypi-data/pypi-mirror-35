from collections import deque

import redis

from messages import Message


class Board(object):
    def put(self, message):
        """
        This will post a message to the board.
        :param Message message:
        """
        raise NotImplementedError()

    def get(self, recipient):
        """
        This will get the next message from the board.

        Boards act like queues, and allow multiple clients to write to them.
        :param str recipient:
        :rtype: Message
        """
        raise NotImplementedError()

    def len(self, recipient):
        """
        This will return the number of messages for `recipient`.
        :param str recipient:
        :rtype: int
        """
        raise NotImplementedError()

    def empty(self, recipient):
        """
        This will return whether there are no messages for `recipient`.
        :param str recipient:
        :rtype: bool
        """
        return self.len(recipient) == 0

    def clear(self):
        """
        This will clear all messages on the board.
        :return:
        """
        raise NotImplementedError()


class MemoryBoard(Board):
    """ This will create a message board that is stored in the processes memory. """
    def __init__(self):
        self._boards = {}

    def put(self, message):
        """
        :param Message message:
        """
        if message.recipient not in self._boards:
            self._boards[message.recipient] = deque([], 1)

        self._boards[message.recipient].append(message)

    def get(self, recipient):
        if recipient not in self._boards:
            return None

        board = self._boards[recipient]
        return board.popleft() if len(board) > 0 else None

    def len(self, recipient):
        if recipient not in self._boards:
            return 0

        return len(self._boards[recipient])

    def clear(self):
        self._boards = {}


class RedisBoard(Board):
    """ This will create a message board that is backed by Redis. """

    def __init__(self, client, key='raft_message_board'):
        """
        :param redis.Redis client:
        """
        self.redis = client
        self.key = key
        self.keys = []

    def __del__(self):
        self.clear()

    def put(self, message):
        self.redis.lpush(self.key + message.recipient, message.serialise())
        self.redis.ltrim(self.key + message.recipient, 0, 0)

    def get(self, recipient):
        message = self.redis.lpop(self.key + recipient)
        return Message.unserialise(message) if message else None

    def len(self, recipient):
        return self.redis.llen(self.key + recipient)

    def clear(self):
        for key in self.redis.keys(self.key + '*'):
            self.redis.delete(key)

