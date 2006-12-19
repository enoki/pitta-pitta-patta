#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

class Rule:
    """ Serves as a base for all pitta pitta patta rules. """

    def __init__(self):
        """ Initializes a new rule. """
        pass

    def is_next(self, card, existing_card):
        """ True if the card is next in the series after existing_card. """
        print "GH"
        return True

    def is_starter(self, card):
        """ True if the card can start a new foundation pile. """
        print "G"
        return True
