#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

class Rules:
    """ Enforces certain rules about pitta pitta patta. """

    def __init__(self, rules):
        """ Initializes a new set of rules. """
        self.rules = rules

    def is_valid(self, card, pile):
        """ True if the card can be put on top of the foundation pile. """
        if pile.empty():
            return self.is_starter(card)

        return self.is_next(card, pile.top_card())

    def is_next(self, card, existing_card):
        """ True if the card is next in the series after existing_card. """
        next = True

        for rule in self.rules:
            next = next and rule.is_next(card, existing_card)

        return next

    def is_starter(self, card):
        """ True if the card can start a new foundation pile. """
        starter = True

        for rule in self.rules:
            starter = starter and rule.is_starter(card)

        return starter
