"""
ActiveNodes take part in all votes, keep track of the consensus log, and immediately converts to a Candidate
on election timeout. """
NODE_MODE_ACTIVE = 1
"""
Passive mode take part in all votes, keep track of the consensus log, but never nominates itself for leadership.
"""
NODE_MODE_PASSIVE = 2
"""
ReluctantNodes take part in all votes, keep track of the consensus log, but only converts to a Candidate if it
receives only request requests from Candidates behind in the consensus log history.
"""
NODE_MODE_RELUCTANT = 3
