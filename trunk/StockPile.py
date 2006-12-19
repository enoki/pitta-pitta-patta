#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Pile import Pile

class StockPile(Pile):
    """ The cards the player holds in his hand during play. """

    def __init__(self):
        Pile.__init__(self)

    def take_from(self, deck):
        """ Take all cards from the deck. Flip them over as well. """
        while not deck.empty():
            card = deck.take_top_card()
            card.face_down()
            self.cards.add_card(card)


