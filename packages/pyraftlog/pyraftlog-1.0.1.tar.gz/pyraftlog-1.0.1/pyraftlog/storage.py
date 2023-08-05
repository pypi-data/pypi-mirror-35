import redis
import cPickle

from states import Follower


class Storage(object):
    def retrieve(self, node):
        """
        Retrieve the state of the given name from storage.
        Must always be a `Follower` as we have that is the default.
        :param pyraftlog.nodes.Node node:
        :return: The loaded state
        :rtype: Follower
        """
        return Follower(node)

    def persist(self, state):
        """
        Persist the given state to storage.
        :param State state:
        :return: True if successful
        :rtype: bool
        """
        return True

    @staticmethod
    def extract_dict(state):
        """
        :param State state:
        :return: A dict containing all the state data that must be persisted
        """
        return {
            "current_term": state.current_term,
            "voted_for": state.voted_for,
            "log": state.log,

            "commit_index": state.commit_index,
            "last_applied": state.last_applied,

            "cluster_applied": state.cluster_applied,
            "log_reduction": state.log_reduction,
        }

    @staticmethod
    def apply_dict(state, stored):
        """
        Update the given `state` with the values in `stored`
        :param State state:
        :param dict stored:
        """
        state.current_term = stored['current_term'] or state.current_term
        state.voted_for = stored['voted_for'] or state.voted_for
        state.log = stored['log'] or state.log

        state.commit_index = stored['commit_index'] or state.commit_index
        state.last_applied = stored['last_applied'] or state.last_applied

        state.cluster_applied = stored['cluster_applied'] or state.cluster_applied
        state.log_reduction = stored['log_reduction'] or state.log_reduction


class RedisStorage(Storage):
    def __init__(self, redis_client, key_prefix='raft_state_'):
        """
        :param redis.Redis redis_client:
        :param str key_prefix:
        """
        self.redis_client = redis_client
        self.key_prefix = key_prefix

    def retrieve(self, node):
        # Retrieve the data from redis
        state = Follower(node)
        value = self.redis_client.get(self.key_prefix + node.name)
        if value:
            value = cPickle.loads(value)
            Storage.apply_dict(state, value)
            node.logger.info("Retrieved state (%2d,%2d)[%2d]" % (value['current_term'], value['commit_index'],
                                                                 len(state.log)))
        return state

    def persist(self, state):
        value = cPickle.dumps(Storage.extract_dict(state), 2)
        self.redis_client.set(self.key_prefix + state.node.name, value)