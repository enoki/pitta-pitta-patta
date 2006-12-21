#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import louie
import logging
from Card import Card
from Pile import Pile


class HomePile(Pile):
    """ The cards the player must get rid of in order to stop the game. """

    emptied = louie.Signal()

    def __init__(self):
        Pile.__init__(self)
        self.initial_size = 13

    def take_from(self, deck):
        """ Take cards from the deck. Flip over the top card. """
        for i in range(self.initial_size):
            self.cards.add_card(deck.take_top_card())

        self.cards.top_card().face_up()

    def squelch(self, card, cell):
        self.remove_card(card)
        cell.set_card(card)
        self.card_taken(card)

    def transfer(self, card, pile):
        Pile.transfer(self, card, pile)
        self.card_taken(card)

    def card_taken(self, card):
        " Called when a card is taken from the top of the home pile. "
        if not self.cards.empty():
            self.top_card().face_up()
        else:
            louie.send(HomePile.emptied)
