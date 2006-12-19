#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from Deck import Deck
from StockPile import StockPile
from HomePile import HomePile
from DiscardPile import DiscardPile
from CellCards import CellCards
from RightHand import RightHand
from CardLocation import CardLocation
from Selection import Selection
import logging


class Player:
    """ A player in the game. """

    def __init__(self):
        self.deck = Deck()

        self.home_pile = HomePile()
        self.cell_cards = CellCards(self.home_pile)
        self.stock_pile = StockPile()
        self.right_hand = RightHand()
        self.discard_pile = DiscardPile()

        self.home_pile.take_from(self.deck)
        self.cell_cards.take_from(self.deck)
        self.stock_pile.take_from(self.deck)

        self.set_locations()

        # Move cards to their proper locations
        self.home_pile.calibrate()
        self.cell_cards.calibrate()
        self.stock_pile.calibrate()

        #
        self.selection = Selection()

        self.drawables = [self.home_pile,
                          self.cell_cards,
                          self.stock_pile,
                          self.discard_pile,
                          self.right_hand,
                          self.selection]

        self.clickables = [self.home_pile,
                           self.cell_cards,
                           self.discard_pile]

        self.xxxcount = 0

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def set_locations(self):
        """ Position cards """
        card_rect = self.home_pile.top_card().rect
        card_width, card_height = card_rect.width, card_rect.height
        left_margin, top_margin = 10, 250
        hand_top_margin = top_margin + card_rect.height + 30

        self.home_pile.move_to(left_margin, top_margin)
        self.stock_pile.move_to(left_margin + card_width * 2, hand_top_margin)
        self.discard_pile.move_to(left_margin + card_width * 2  + card_width * 1.5, hand_top_margin)
        self.cell_cards.move_to(left_margin + card_width * 2, top_margin, card_width * 1.5)
        self.right_hand.move_to(left_margin + card_width * 2 + card_width * 1.5 * 2, hand_top_margin, 40)


    def handle(self, event):
        """ Handle events that the player knows about. """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_left_mouse_down(event)

            elif event.button == 3:
                self.handle_right_mouse_down(event)

    def handle_left_mouse_down(self, event):
        """ Handle a left click. """
        x, y = event.pos[0], event.pos[1]

        for clickable in self.clickables:
            card = clickable.get_card(x, y)
            if card is not None:
                self.selection.set(card, clickable)
                return

    def handle_right_mouse_down(self, event):
        """ Handle a right click. """
        # Shuffle from stock_pile to discard_pile
        # Place in hand if count < 3,
        # otherwise place in discard pile, count = 0
        if self.xxxcount != 0 and self.stock_pile.cards.empty():
            self.xxxcount = 3

        self.xxxcount += 1
        if self.xxxcount == 4:
            self.discard_pile.take_from(self.right_hand.cards)
            self.discard_pile.calibrate()
            self.xxxcount = 0
        else:
            if self.stock_pile.cards.empty():
                self.stock_pile.take_from(self.discard_pile.cards)
                self.stock_pile.calibrate()

            self.right_hand.take_from(self.stock_pile.cards)
            self.right_hand.calibrate()
            logging.warning('rh=' + str(self.right_hand.cards.top_card().number()))

        if not self.discard_pile.empty():
            logging.warning('di' + str(self.discard_pile.top_card().number()))

    def get_selection(self):
        """ Returns the current selection. """
        return self.selection

    def has_selection(self):
        """ Returns true if there is a card selected. """
        return not self.selection.empty()

    def clear_selection(self):
        self.selection.clear()
