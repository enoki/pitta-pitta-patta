#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

class SkillLevel:
    """ The skill level of a computer player. """

    def get_time_between_moves(self):
        """ The time to think between moves. """

    def get_time_to_deal_one_card(self):
        """ The time to take to deal one card from the Stock Pile. 
            Typically faster. """

    def get_time_between_deals(self):
        """ The time taken to look at a new card in the Discard Pile.
            Typically slower. """

    def should_consider_playable(self):
        """ Returns true if a playable card should be considered.
            Typically random. """

    def max_piles_to_consider(self):
        """ Returns the maximum number of foundation piles to consider
            at any one time. """

    def should_consider_discard_pile(self):
        """ Returns true if the new discard pile card should be considered.
            Typically random. """
