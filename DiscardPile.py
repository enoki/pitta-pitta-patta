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
        cards = right_hand.rip_cards()
        cards.reverse()

        for card in cards:
            card.face_up()
            self.cards.add_card(card)

    def calibrate(self):
        """ Prepare cards for display. """
        Pile.calibrate(self)
        self.cards.top_card().face_up()

