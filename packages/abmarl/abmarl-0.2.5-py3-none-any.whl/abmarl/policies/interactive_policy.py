
from pprint import pprint

from abmarl.policies.policy import Policy


class InteractivePolicy(Policy):
    def compute_action(self, obs, **kwargs):
        pprint(obs)
