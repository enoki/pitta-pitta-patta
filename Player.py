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
from Card import Card
from Pile import Pile
from CardCell import CardCell
from CellCards import CellCards
from RightHand import RightHand
from CardLocation import CardLocation
from Selection import Selection


class Player:
    """ A player in the game. """

    finished = louie.Signal()

    def __init__(self, name, deck_name, game_config):
        self.deck = Deck(deck_name)

        self.home_pile = HomePile(game_config.home_pile_size)
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

        # Start out with cell cards face down
        for cell in self.cell_cards.each_cell():
            cell.face_down()

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

        self.updateables = []

        self.xxxcount = 0

        self.score = 0

        self.cards_in_transit = []

        self.name = name

        louie.connect(self.card_grabbed, Card.grabbed)
        louie.connect(self.card_thrown, Card.thrown)
        louie.connect(self.home_emptied, HomePile.emptied)

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

        for card in self.cards_in_transit:
            card.draw(surface)

    def set_locations(self):
        """ Position cards """
        some_card = self.home_pile.top_card()
        card_width, card_height = some_card.rect.width, some_card.rect.height
        left_margin, top_margin = 15, 450
        hand_top_margin = top_margin + card_height + 10

        x, y = left_margin, top_margin

        # Top row
        self.home_pile.move_to(x, y)
        x += card_width * 1.7
        distance_between = card_width * 1.3
        self.cell_cards.move_to(x, y, distance_between)

        x = left_margin + card_width * 0.2
        y = hand_top_margin

        # Bottom row
        self.stock_pile.move_to(x, y)
        x += card_width * 1.5
        self.discard_pile.move_to(x, y)
        x += card_width * 1.5
        self.right_hand.move_to(x, y, 40)


    def update(self):
        for updateable in self.updateables:
            updateable.update()

        for card in self.cards_in_transit:
            card.update()

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
                if not self.selection.empty() and \
                       self.selection.card == card:
                    # Clear the selection if the card is already selected
                    self.selection.clear()
                else:
                    # Otherwise select the card
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

            if self.has_selection() and \
               self.selection.home == self.discard_pile:
                # Clear the selection if it's the discard pile
                self.clear_selection()
        else:
            if self.stock_pile.cards.empty():
                self.stock_pile.take_from(self.discard_pile.cards)
                self.stock_pile.calibrate()

            self.right_hand.take_from(self.stock_pile.cards)
            self.right_hand.calibrate()

    def home_emptied(self):
        louie.send(Player.finished)

    def inc_score(self):
        self.score += 1

    def get_score(self):
        """ Returns the total score """
        return self.num_good_cards() - self.num_bad_cards() * 2

    def num_good_cards(self):
        """ Returns the number of cards put out """
        return self.score

    def num_bad_cards(self):
        """ Returns the number of cards still in the home pile """
        return self.home_pile.cards.num_cards()

    def card_thrown(self, card):
        self.cards_in_transit.append(card)

    def card_grabbed(self, card):
        self.cards_in_transit.remove(card)

    def get_selection(self):
        """ Returns the current selection. """
        return self.selection

    def has_selection(self):
        """ Returns true if there is a card selected. """
        return not self.selection.empty()

    def clear_selection(self):
        self.selection.clear()

    def get_name(self):
        return self.name

    def flip_cell(self, cell_index):
        self.cell_cards.get_cell(cell_index).flip()
