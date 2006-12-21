#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Rule import Rule

class RedBlackRule(Rule):
    """ Enforces the rule that cards must alternative colors. """

    def __init__(self):
        pass

    def is_next(self, card, existing_card):
        """ True if the card is next in the series after existing_card. """
        return card.color() != existing_card.color()
