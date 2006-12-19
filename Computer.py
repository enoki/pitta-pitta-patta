#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import logging
from Deck import Deck
from CardGroup import CardGroup

class Computer:
    """ The computer AI player. """

    def __init__(self, rules, foundation_piles):
        self.cards = Deck()
        self.discard = CardGroup()
        self.rules = rules
        self.foundation_piles = foundation_piles
        self.last_time = pygame.time.get_ticks()

    def draw(self, surface):
        pass

    def handle(self, event):
        pass

    def update(self):
        if pygame.time.get_ticks() - self.last_time > 1000:
            logging.warning("** Computer tick")
            self.last_time = pygame.time.get_ticks()

            if self.cards.empty():
                if self.discard.empty():
                    logging.warning("** Computer is done.")
                    return
                self.discard.shuffle()
                while not self.discard.empty():
                    self.cards.add_card(self.discard.take_top_card())

            card = self.cards.take_top_card()
            logging.warning("** Computer card=" + str(card))
            for pile in self.foundation_piles.piles:
                if self.rules.is_valid(card, pile):
                    pile.add_card(card)
                    pile.calibrate()
                    return

            self.discard.add_card(card)

# TODO make this more like a real player, with the same restrictions!
# TODO idea: MockHomePile, MockDiscardPile, MockCellCards, etc...
