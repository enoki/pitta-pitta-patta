#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Deck import Deck
from StockPile import StockPile
from HomePile import HomePile
from DiscardPile import DiscardPile
from Pile import Pile
from CardCell import CardCell
from CellCards import CellCards
from RightHand import RightHand
from CardLocation import CardLocation
from Selection import Selection
import logging


class Player:
    """ A player in the game. """

    finished = louie.Signal()

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

        self.score = 0

        louie.connect(self.card_grabbed, Pile.grabbed_card)
        louie.connect(self.card_grabbed, CardCell.grabbed_card)
        louie.connect(self.home_emptied, HomePile.emptied)

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def set_locations(self):
        """ Position cards """
        card_rect = self.home_pile.top_card().rect
        card_width, card_height = card_rect.width, card_rect.height
        left_margin, top_margin = 10, 500
        hand_top_margin = top_margin + card_rect.height + 30

        self.home_pile.move_to(left_margin, top_margin)
        self.stock_pile.move_to(left_margin + card_width * 2, hand_top_margin)
        self.discard_pile.move_to(left_margin + card_width * 2  + card_width * 1.5, hand_top_margin)
        self.cell_cards.move_to(left_margin + card_width * 2, top_margin, card_width * 1.5)
        self.right_hand.move_to(left_margin + card_width * 2 + card_width * 1.5 * 2, hand_top_margin, 40)


    def update(self):
        pass

    def handle(self, event):
        """ Handle events that the player knows about. """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_left_mouse_down(event)

            elif event.button == 3:
                self.handle_right_mouse_down(event)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.handle_space_bar()

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
        self.deal_card()

    def handle_space_bar(self):
        """ Handle a space bar keypress. """
        self.deal_card()

    def deal_card(self):
        """ Shuffle from stock_pile to discard_pile
            Place in hand if count < 3,
            otherwise place in discard pile, count = 0 """

        if self.xxxcount != 0 and self.stock_pile.cards.empty():
            self.xxxcount = 3

        self.xxxcount += 1
        if self.xxxcount == 4:
            self.discard_pile.take_from(self.right_hand)
            self.discard_pile.calibrate()
            self.xxxcount = 0
        else:
            if self.stock_pile.cards.empty():
                self.stock_pile.take_from(self.discard_pile.cards)
                self.stock_pile.calibrate()

            self.right_hand.take_from(self.stock_pile.cards)
            self.right_hand.calibrate()
            logging.warning('rh=' + str(self.right_hand.top_card().number()))

        if not self.discard_pile.empty():
            logging.warning('di' + str(self.discard_pile.top_card().number()))

    def home_emptied(self):
        louie.send(Player.finished)

    def inc_score(self):
        self.score += 1
        logging.debug('score one for ' + __name__ + ', tot=' + str(self.score))

    def get_score(self):
        num_bad_cards = self.home_pile.cards.num_cards()
        return self.score - num_bad_cards * 2

    def card_grabbed(self, card):
        logging.warning('card grabbed=' + str(card))
        pass

    def get_selection(self):
        """ Returns the current selection. """
        return self.selection

    def has_selection(self):
        """ Returns true if there is a card selected. """
        return not self.selection.empty()

    def clear_selection(self):
        self.selection.clear()
