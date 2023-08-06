import random

from logs import Log
from messages import Message


class State(object):
    APPEND_MAX = 100

    def __init__(self, node=None):
        """
        :param pyraftlog.nodes.Node node:
        """
        self.node = node
        # Persistent state on all nodes
        # latest term server has seen (increases monotonically)
        self.current_term = 0
        # candidate id that received vote in current term
        self.voted_for = {}
        # log entries; each entry contains command for state machine, and term when entry was received by leader
        self.log = Log()

        # Volatile state on all nodes
        # index of highest log entry known to be committed (increases monotonically)
        self.commit_index = 0
        # index of highest log entry applied to state machine (increases monotonically)
        self.last_applied = 0

        # Added values for log reduction
        self.cluster_applied = {node.name: 0} if node else None
        self.log_reduction = False

        # Volatile state on leaders
        # for each node, index of the index log entry to send to that node
        self.next_index = {}
        # for each node, index of highest log entry known to be replicated on node (increases monotonically)
        self.match_index = {}
        for neighbour in node.neighbours if node else []:
            self.next_index[neighbour] = self.log.next_index(self.log.index())
            self.match_index[neighbour] = 0

        # Volatile state on candidates
        self.votes = {}

    def __setstate__(self, state):
        self.__init__()
        self.__dict__.update(state)

    def __getstate__(self):
        return {
            "current_term": self.current_term,
            "voted_for": self.voted_for,
            "log": self.log,

            "commit_index": self.commit_index,
            "last_applied": self.last_applied,

            "cluster_applied": self.cluster_applied,
            "log_reduction": self.log_reduction,
        }

    @classmethod
    def from_state(cls, from_state, message_term=None):
        """
        Create a state based on `from_state`.
        :param State from_state:
        :param int message_term:
        :rtype: State
        """
        state = cls(from_state.node)
        state.populate(from_state)
        if message_term:
            state.current_term = message_term

        return state

    def populate(self, from_state):
        self.current_term = from_state.current_term
        self.voted_for = from_state.voted_for
        self.log = from_state.log

        self.commit_index = from_state.commit_index
        self.last_applied = from_state.last_applied

        self.cluster_applied = from_state.cluster_applied
        self.log_reduction = from_state.log_reduction

    def next_timeout_time(self):
        """ Generate a new timeout. """
        return random.randrange(self.node.election_timeout, 2 * self.node.election_timeout) / 1000.0

    def on_leader_timeout(self):
        """
        This is called when the leader timeout is reached.
        :rtype: State
        """
        return self

    def on_vote_request(self, message):
        """
        This is called when there is a vote request.
        :param Message message: The vote requested message
        :rtype: State, Message
        """
        self.node.logger.debug("[%-9s] Vote request received from %s" % (self.__class__.__name__, message.sender))

        data = message.data
        # If the candidate's term is behind ours
        if message.term < self.current_term:
            return self, self.vote_response_message(data['candidate_id'], False)

        # If we haven't voted this term or we voted for this candidate and
        if self.current_term not in self.voted_for or self.voted_for[self.current_term] == data['candidate_id']:
            # If candidate's log is at least as up-to-date as ours
            if self.log.index() <= data['last_log_index']:
                self.node.logger.debug("[%-9s] Casting vote for %s" % (self.__class__.__name__, message.sender))
                self.voted_for = {self.current_term: data['candidate_id']}
                # persist changes
                self.node.storage.persist(self)
                return self, self.vote_response_message(data['candidate_id'], True)

        return self, self.vote_response_message(data['candidate_id'], False)

    def on_vote_response(self, message):
        """
        This is called when this node receives a vote.
        :param Message message: The vote received message
        :rtype: State, Message
        """
        self.node.logger.debug("[%-9s] Vote response received: %s" % (self.__class__.__name__, message))
        return self, None

    def on_append_entries(self, message):
        """
        This is called when there is a request to append an entry to the log.
        :param Message message: The append entries message
        :rtype: State, Message
        """
        data = message.data

        # Reply false if the message term < our current term
        if message.term < self.current_term:
            self.node.logger.info("Ahead of term (%2d < %2d)" % (message.term, self.current_term))
            return self, self.append_response_message(message.sender, False)

        # extend timeout time
        self.node.extend_timeout()

        # fail fast if prev log index has been reduced
        if self.log.tail().index > data['prev_log_index']:
            return self, self.append_response_message(message.sender, False)

        # can't be up to date if our log is smaller than prev log index
        if self.log.index() < data['prev_log_index']:
            self.node.logger.info("Behind log index (%2d < %2d)" % (self.log.index(), data['prev_log_index']))
            return self, self.append_response_message(message.sender, False)

        # If our term doesn't match the leaders
        if self.log.get(data['prev_log_index']).term != data['prev_log_term']:
            entry = self.log.get(data['prev_log_index'])
            self.node.logger.info("Inconsistent logs (%2d,%2d) != (%2d,%2d)" % (entry.term, entry.index,
                                                                                data['prev_log_term'],
                                                                                data['prev_log_index']))
            if self.log.tail().index <= data['prev_log_index']:
                self.log.rewind(data['prev_log_index'] - 1)
            return self, self.append_response_message(message.sender, False)

        # The induction proof held so we append any new entries
        self.node.logger.debug("Appending entries")
        index = data['prev_log_index']
        for e in data['entries']:
            index += 1
            self.node.logger.info("Considering entry: (%2d,%2d)" % (e.term, e.index))
            # If an existing entry conflicts with a new one trust the leaders log
            if self.log.index() >= index and self.log.get(index).term != e.term:
                entry = self.log.get(index)
                self.node.logger.info("Inconsistent logs (%2d,%2d) != (%2d,%2d)" % (entry.term, entry.index,
                                                                                    e.term, e.index))
                if self.log.tail().index <= data['prev_log_index']:
                    self.log.rewind(index - 1)

            # Append any new entries not already in the log
            if self.log.index() < index:
                self.node.logger.info("Appending entry to log: %s" % e.value)
                self.log.append(e.term, e.value)

        # Update our commit index
        if data['leader_commit'] > self.commit_index:
            self.commit_index = min(data['leader_commit'], self.log.index())

        # Update our cluster_applied and log reduction
        self.cluster_applied = data['cluster_applied']
        self.log_reduction = data['log_reduction']
        # Reduce the log
        if self.log_reduction:
            if self.log.reduce(min(self.cluster_applied.values())):
                self.node.logger.debug("[%-9s] Reduced log: %2d" % (self.__class__.__name__, len(self.log)))

        # persist changes
        self.node.storage.persist(self)

        return self, self.append_response_message(message.sender, True)

    def on_append_response(self, message):
        """ This is called when a response is sent back to the Leader. """
        return self, None

    def append_log_entry(self, command):
        pass

    def vote_response_message(self, candidate, response):
        return Message(Message.VOTE_RESPONSE, self.node.name, candidate, self.current_term, {
            "response": response
        })

    def append_response_message(self, recipient, response):
        return Message(Message.APPEND_RESPONSE, self.node.name, recipient, self.current_term, {
            "response": response,
            "last_applied": self.last_applied,

            # Inform the leader the head of our log
            "last_appended": self.log.index(),
        })


class Leader(State):
    def populate(self, from_state):
        super(Leader, self).populate(from_state)

        for neighbour in self.node.neighbours:
            self.next_index[neighbour] = self.log.next_index(self.log.index())

    def next_timeout_time(self):
        """ Generate a new timeout. """
        return self.node.heartbeat_timeout / 1000.0

    def on_leader_timeout(self):
        """ This is called when the leader (self) timeout is reached. """
        self.node.logger.debug("[%-9s] Firing heartbeat" % self.__class__.__name__)
        self.send_heartbeats()
        self.node.extend_timeout()
        return self

    def on_append_response(self, message):
        response = None
        data = message.data
        if not data['response']:
            # Attempt to catch up the node that is behind
            if self.next_index[message.sender] > 0:
                self.next_index[message.sender] = self.log.prev_index(self.next_index[message.sender])
                response = self.append_entry_message(message.sender)
        else:
            # Update the match next indexes for the message sender
            self.match_index[message.sender] = min(self.log.index(), self.next_index[message.sender])
            self.next_index[message.sender] = min(self.log.index() + 1, self.log.next_index(data['last_appended']))

            # Respond with next entry if still behind
            if self.next_index[message.sender] <= self.log.index():
                response = self.append_entry_message(message.sender)

            # update commit index if there is a majority
            for index in sorted(self.match_index.values(), reverse=True):
                if index > self.commit_index:
                    count = sum(1 for x in self.match_index.values() if x >= index)
                    if self.node.has_majority(count + 1):
                        self.commit_index = index
                        # persist changes
                        self.node.storage.persist(self)

            # Update `cluster_applied`
            self.cluster_applied[message.sender] = data['last_applied']

        # Perform log reduction
        if self.log_reduction:
            if self.log.reduce(min(self.cluster_applied.values())):
                self.node.logger.debug("[%-9s] Reduced log: %2d" % (self.__class__.__name__, len(self.log)))
                # persist changes
                self.node.storage.persist(self)

        if response:
            self.node.logger.debug("[%-9s] Response message: %s" % (self.__class__.__name__, response))

        return self, response

    def send_heartbeats(self):
        """
        Sends a heartbeat to every neighbour.
        """
        for neighbour in self.node.neighbours:
            if self.node.message_board.empty(neighbour):
                self.send_heartbeat(neighbour)

    def send_heartbeat(self, neighbour):
        """
        Sends a heartbeat to `neighbour` if there are no other messages queued.
        :param str neighbour:
        """
        if self.node.message_board.len(neighbour) == 0:
            self.node.post_message(self.append_entry_message(neighbour, True))

    def append_log_entry(self, command):
        index = self.log.append(self.current_term, command)
        self.node.logger.debug("[%-9s] Appended log entry (%2d,%2d)" % (self.__class__.__name__,
                                                                        self.current_term,
                                                                        self.log.index()))

        # persist changes
        self.node.storage.persist(self)

        # send this entry to out to neighbours who are up-to-date
        for neighbour in self.node.neighbours:
            if self.next_index[neighbour] == self.log.next_index() - 1:
                self.node.post_message(self.append_entry_message(neighbour))

        return index

    def append_entry_message(self, recipient, heartbeat=False):
        next_log_index = self.next_index[recipient]
        prev_log_index = self.log.prev_index(next_log_index)
        entries = [] if heartbeat else self.log.slice(next_log_index, self.APPEND_MAX)

        return Message(Message.APPEND_ENTRIES, self.node.name, recipient, self.current_term, {
            "leader_id": self.node.name,
            "prev_log_index": prev_log_index,
            "prev_log_term": self.log.get(prev_log_index).term,
            "entries": entries,
            "leader_commit": self.commit_index,

            # Inform followers of request address for clients
            "request_address": self.node.request_address,

            # Inform followers of whether log reduction is active
            # and where the whole cluster is up to
            "log_reduction": self.log_reduction,
            "cluster_applied": self.cluster_applied,
        })


class Candidate(State):
    def populate(self, from_state):
        super(Candidate, self).populate(from_state)
        self.current_term += 1

    def next_timeout_time(self):
        """ Generate a new timeout. """
        return self.node.vote_timeout / 1000.0

    def on_leader_timeout(self):
        """ Start election! """
        self.node.logger.info("[%-9s] Starting election" % self.__class__.__name__)
        if self.current_term not in self.voted_for or len(self.votes) > 1:
            self.current_term += 1
        self.voted_for = {self.current_term: self.node.name}
        self.votes = {self.node.name: True}
        # persist changes
        self.node.storage.persist(self)
        for neighbour in self.node.neighbours:
            self.node.post_message(self.vote_request_message(neighbour))

        self.node.extend_timeout()
        return self

    def on_vote_response(self, message):
        self.node.logger.debug("[%-9s] Received vote from %s: %r" % (self.__class__.__name__,
                                                                     message.sender, message.data['response']))
        # Update the votes tally
        self.votes[message.sender] = message.data['response']

        # If we have successfully received a majority
        if self.node.has_majority(self.votes.values().count(True)):
            # Promote yourself to leader
            self.node.logger.warn("[%-9s] Converting to Leader (%2d|%2d,%2d)" % (self.__class__.__name__,
                                                                                 self.current_term,
                                                                                 self.log.head().term,
                                                                                 self.log.head().index))
            state = Leader.from_state(self)
            # Send the initial heartbeat
            self.node.message_board.clear()
            state.send_heartbeats()
            self.node.extend_timeout(state)
            return state, None
        else:
            return self, None

    def on_append_entries(self, message):
        """
        Convert to follower and call the follower append entries.
        :rtype: State, Message
        """
        self.node.logger.info("[%-9s] Converting to follower" % self.__class__.__name__)
        return Follower.from_state(self).on_append_entries(message)

    def vote_request_message(self, recipient):
        return Message(Message.VOTE_REQUEST, self.node.name, recipient, self.current_term, {
            "candidate_id": self.node.name,
            "last_log_index": self.log.index(),
            "last_log_term": self.log.head().term if self.log else 0,
        })


class Follower(State):
    def on_leader_timeout(self):
        """ Convert to a candidate and immediately start an election. """
        self.node.logger.info("[%-9s] Election timeout reached" % self.__class__.__name__)
        return Candidate.from_state(self).on_leader_timeout()
