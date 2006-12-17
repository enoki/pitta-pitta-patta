#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Pile import Pile


class HomePile(Pile):
    """ The cards the player must get rid of in order to stop the game. """
    def __init__(self):
        Pile.__init__(self)
        self.initial_size = 13

    def take_from(self, deck):
        """ Take cards from the deck. Flip over the top card. """
        for i in range(self.initial_size):
            self.cards.add_card(deck.take_top_card())

        self.cards.top_card().frontSide()

    def transfer(self, card, pile):
        Pile.transfer(self, card, pile)
        if not self.cards.empty():
            self.top_card().frontSide()
