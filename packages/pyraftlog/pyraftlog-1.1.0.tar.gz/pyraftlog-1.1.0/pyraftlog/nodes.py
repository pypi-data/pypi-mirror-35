import logging
import pyraftlog
import threading

from boards import MemoryBoard
from messages import Message
from states import Follower
from states import Leader
from storage import Storage


class Node(object):
    def __init__(self, mode, name, neighbourhood, storage,
                 election_timeout=500, heartbeat_timeout=250, vote_timeout=150,
                 logger=None):
        """
        :param int mode: Initial node mode
        :param str name: Name of node
        :param str[] neighbourhood: List of neighbours
        :param Storage storage: Storage for the state
        :param int election_timeout: election timeout in milliseconds
        :param int heartbeat_timeout: leader heartbeat timeout
        :param int vote_timeout: candidate vote timeout
        :param logging.Logger logger:
        """
        self.mode = mode
        self.name = name
        self.neighbourhood = neighbourhood
        self.election_timeout = election_timeout
        self.heartbeat_timeout = heartbeat_timeout
        self.vote_timeout = vote_timeout
        self.storage = storage
        self.message_board = MemoryBoard()
        self.lock = threading.Lock()
        self.leader = (None, None)
        self.request_address = None
        self.logger = logger or logging.getLogger(__name__)

        # Neighbours is everyone in the neighbourhood but us
        self.neighbours = list(self.neighbourhood)
        self.neighbours.remove(self.name)

        self.state = storage.retrieve(self)

        self.logger.info("Neighbourhood: %s" % repr(self.neighbourhood))

        # Activate
        self.timeout_timer = None
        self.timeout_count = 0
        self.extend_timeout()
        self.leadership_required = False

        # Auto applier
        self.auto_apply = True
        self.applier = threading.Thread(target=self.entry_applier, args=[self])
        self.applier.daemon = True
        self.applier.start()

    def __del__(self):
        if self.timeout_timer is not None:
            self.timeout_timer.cancel()

    def is_leader(self):
        """
        :return: True if Leader, false otherwise
        :rtype: bool
        """
        return isinstance(self.state, Leader)

    def get_leader(self):
        """
        :return: The current leader
        :rtype: str
        """
        return self.name if self.is_leader() else self.leader[0]

    def get_request_address(self):
        return self.request_address if self.is_leader() else self.leader[1]

    def has_majority(self, count):
        """
        :param int count:
        :return: True if count is a majority
        """
        return count > int((len(self.neighbourhood) - 1) / 2)

    def post_message(self, message):
        self.logger.debug("[%-9s] Posting message: %s" % (self.state.__class__.__name__, message))
        self.message_board.put(message)

    def on_message(self, message):
        """
        This is called when a message is received.
        :param Message message:
        :return: Response
        :rtype: Message
        """
        with self.lock:
            self.logger.debug("[%-9s] Message received: %s" % (self.state.__class__.__name__, message))
            state = self.state

            # If request/response message term > current term become a follower
            if message.term > self.state.current_term:
                self.logger.info("Behind term %s (%2d -> %2d)" % (message.sender, self.state.current_term, message.term))
                state = Follower.from_state(state, message.term)
                self.state = state

            # Perform action based on message type and current state
            response = None
            if message.type == Message.APPEND_ENTRIES:
                self.leader = (message.sender, message.data['request_address'])
                state, response = state.on_append_entries(message)
            elif message.type == Message.VOTE_REQUEST:
                state, response = state.on_vote_request(message)
                # Leadership is required if there isn't an eligible candidate
                self.leadership_required = self.state.current_term not in self.state.voted_for
                if self.mode == pyraftlog.NODE_MODE_RELUCTANT and self.leadership_required:
                    self.logger.info("[%-9s] No eligible candidate" % self.state.__class__.__name__)
            elif message.type == Message.VOTE_RESPONSE:
                state, response = state.on_vote_response(message)
            elif message.type == Message.APPEND_RESPONSE:
                state, response = state.on_append_response(message)
                # Leadership is still required while the majority of nodes are behind
                self.leadership_required = self.state.log.index() != self.state.match_index[message.sender]
                if self.mode == pyraftlog.NODE_MODE_RELUCTANT and not self.leadership_required:
                    self.logger.info("[%-9s] Candidate now eligible" % self.state.__class__.__name__)

            # Applying entries is performed in a daemon thread

            # Update the current state
            self.state = state

            # Post the response if one provided
            if response and response.recipient in self.neighbours:
                self.logger.debug("[%-9s] Response message: %s" % (self.state.__class__.__name__, message))
                return response
            return None

    @staticmethod
    def entry_applier(node):
        node.logger.debug('Starting entry applier')
        while True:
            # If commit index > last applied and not set to auto apply
            if node.auto_apply and node.state.commit_index > node.state.last_applied:
                node.apply_entry(node.state)

    def apply_entry(self, state):
        """
        Apply the next entry
        :param state:
        """
        # increment the state's last applied
        state.last_applied += 1
        state.cluster_applied[self.name] = state.last_applied

        # persist changes
        self.storage.persist(state)

        self.logger.debug("[%-9s] Applied entry: %s" % (self.state.__class__.__name__, state.last_applied))

    def extend_timeout(self, state=None):
        """ Extend the time when the state will timeout. """
        if self.timeout_timer is not None:
            self.timeout_timer.cancel()

        # In passive mode nothing happens on election timeout
        if self.mode == pyraftlog.NODE_MODE_PASSIVE:
            return

        state = state or self.state

        timeout_time = state.next_timeout_time()
        self.timeout_timer = threading.Timer(timeout_time, self.on_election_timeout, args=[++self.timeout_count])
        self.timeout_timer.start()
        self.logger.debug("[%-9s] Timeout extended by %f" % (state.__class__.__name__, timeout_time))

    def on_election_timeout(self, count):
        # In reluctant mode only do something if leadership is (still) required
        if self.mode == pyraftlog.NODE_MODE_RELUCTANT and not self.leadership_required:
            self.logger.info("[%-9s] Leadership not required" % self.state.__class__.__name__)
            self.extend_timeout()
            return

        with self.lock:
            if count < self.timeout_count:
                self.logger.critical('Behind the times!')
                return
            self.leader = (None, None)
            self.state = self.state.on_leader_timeout()
