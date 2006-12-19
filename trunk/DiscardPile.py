#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Pile import Pile


class DiscardPile(Pile):
    """ The cards the player shuffles from their hand, from the Stock Pile. """
    def __init__(self):
        Pile.__init__(self)

    def take_from(self, right_hand):
        """ Take the cards from the hand."""
        while not right_hand.empty():
            card = right_hand.take_top_card()
            card.frontSide()
            self.cards.add_card(card)

    def calibrate(self):
        """ Prepare cards for display. """
        Pile.calibrate(self)
        self.cards.top_card().frontSide()

