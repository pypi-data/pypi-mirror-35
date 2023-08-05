from collections import deque


class Log(object):
    def __init__(self, iterable=()):
        """
        :param iterable iterable:
        """
        self.entries = deque(iterable)

    def __len__(self):
        return len(self.entries)

    def index(self):
        """
        :return: Latest index in the log
        """
        return self.entries[-1][1] if self.entries else 0

    def get(self, idx):
        """
        :param int idx:
        :return: (term, index, value)
        :rtype: tuple
        """
        for e in reversed(self.entries):
            if e[1] == idx:
                return e

        return 0, 0, None

    def contains(self, idx):
        """
        :param int idx:
        :return: (term, index, value)
        :rtype: tuple
        """
        for e in reversed(self.entries):
            if e[1] == idx:
                return True

        return False

    def head(self):
        """
        :return: (term, index, value)
        :rtype: tuple
        """
        return self.entries[-1] if self.entries else (0, 0, None)

    def tail(self):
        """
        :return: (term, index, value)
        :rtype: tuple
        """
        return self.entries[0] if self.entries else (0, 0, None)

    def prev_index(self, index):
        if not self.entries or self.entries[-1][1] < index:
            return self.entries[-1][1] if self.entries else 0

        for e in reversed(self.entries):
            if e[1] < index:
                return e[1]

        return 0

    def next_index(self, index=None):
        if index is None:
            return self.index() + 1

        if not self.entries or self.entries[0][1] > index:
            return self.entries[0][1] if self.entries else 1

        for e in self.entries:
            if e[1] > index:
                return e[1]

        return self.entries[-1][1] + 1

    def values(self, i, j):
        """
        :param int i:
        :param int j:
        :return: List of all log values from `i` to `j`
        :rtype: list
        """
        values = []
        for e in self.entries:
            if e[1] > j:
                break
            if e[1] >= i:
                values.append({
                    "term": e[0],
                    "index": e[1],
                    "value": e[2],
                })

        return values

    def append(self, entry):
        """
        :param tuple entry: (term, index, value)
        """
        self.entries.append(entry)

    def reduce(self, index):
        """
        Remove all entries in the log with an index less than `index`.
        :param int index:
        :return: True if log effected
        :rtype: bool
        """
        effected = False
        while self.entries and index > self.tail()[1]:
            self.entries.popleft()
            effected = True

        return effected

    def rewind(self, index):
        """
        Remove all entries in the log with an index greater than `index`.
        :param int index:
        :return: True if log effected
        :rtype: bool
        """
        effected = False
        while self.entries and index < self.head()[1]:
            self.entries.pop()
            effected = True

        return effected