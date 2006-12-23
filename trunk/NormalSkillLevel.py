#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import random
from SkillLevel import SkillLevel

class NormalSkillLevel(SkillLevel):
    """ The skill level of a normal computer player. """

    def get_time_between_moves(self):
        """ The time to think between moves. """
        return random.randint(2000, 3000)

    def get_time_to_deal_one_card(self):
        """ The time to take to deal one card from the Stock Pile. """
        return random.randint(450, 600)

    def get_time_between_deals(self):
        """ The time taken to look at a new card in the Discard Pile. """
        return random.randint(800, 1000)

    def should_consider_playable(self):
        """ Returns true if a playable card should be considered. """
        return random.random() < 0.85

    def max_piles_to_consider(self):
        """ Returns the maximum number of foundation piles to consider
            at any one time. """
        return 4

    def should_consider_discard_pile(self):
        """ Returns true if the new discard pile card should be considered. """
        return random.random() < 0.8
