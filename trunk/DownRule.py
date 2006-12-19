#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Rule import Rule
from Card import Card

class DownRule(Rule):
    """ Enforces the rule that cards must descend downwards. """

    def __init__(self):
        pass

    def is_starter(self, card):
        """ True if the card can start a new foundation pile. """
        return card.number() == Card.King

    def is_next(self, card, existing_card):
        """ True if the card is next in the series after existing_card. """
        return card.number() == existing_card.number()-1
