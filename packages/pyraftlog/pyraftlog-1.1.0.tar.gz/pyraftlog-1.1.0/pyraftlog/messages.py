import cPickle


class Message(object):
    APPEND_ENTRIES = 1
    APPEND_RESPONSE = 2
    VOTE_REQUEST = 3
    VOTE_RESPONSE = 4

    def __init__(self, message_type, sender, recipient, term, data):
        """
        :param int message_type:
        :param str sender:
        :param str recipient:
        :param int term:
        :param dict data:
        """
        self.type = message_type
        self.sender = sender
        self.recipient = recipient
        self.term = term
        self.data = data

    def __str__(self):
        if self.type == Message.APPEND_ENTRIES:
            m_type = "APPEND_ENTRIES"
        elif self.type == Message.APPEND_RESPONSE:
            m_type = "APPEND_RESPONSE"
        elif self.type == Message.VOTE_REQUEST:
            m_type = "VOTE_REQUEST"
        elif self.type == Message.VOTE_RESPONSE:
            m_type = "VOTE_RESPONSE"
        else:
            m_type = "UNKNOWN(%d)" % self.type

        return "{0}[{1}]({2}:{3}|{4})".format(m_type, self.term, self.sender, self.recipient, self.data)

    def serialise(self):
        return cPickle.dumps(self)

    @staticmethod
    def unserialise(string):
        return cPickle.loads(string)
