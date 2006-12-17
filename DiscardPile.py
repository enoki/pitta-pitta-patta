#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Pile import Pile


class DiscardPile(Pile):
    """ The cards the player shuffles from their Stock Pile. """
    def __init__(self):
        Pile.__init__(self)

    def take_from(self, stock_pile):
        """ Take the top card from the stock pile."""
        self.cards.add_card(stock_pile.cards.take_top_card())

    def calibrate(self):
        """ Prepare cards for display. """
        Pile.calibrate(self)
        self.cards.top_card().frontSide()

