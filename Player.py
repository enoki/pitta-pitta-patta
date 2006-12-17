import pygame
from Deck import Deck
from StockPile import StockPile
from HomePile import HomePile
from DiscardPile import DiscardPile
from CellCards import CellCards
from CardLocation import CardLocation


class Player:
    """ A player in the game. """

    def __init__(self):
        self.deck = Deck()

        self.home_pile = HomePile()
        self.cell_cards = CellCards()
        self.stock_pile = StockPile()
        self.discard_pile = DiscardPile()

        # This may need to be more global...
        self.selected_card = None

        self.home_pile.take_from(self.deck)
        self.cell_cards.take_from(self.deck)
        self.stock_pile.take_from(self.deck)

        # Add cards back to the deck
        for card in self.home_pile.cards.all_cards():
            self.deck.add_card(card)
        for card in self.cell_cards.cards.all_cards():
            self.deck.add_card(card)
        for card in self.stock_pile.cards.all_cards():
            self.deck.add_card(card)

        # Position cards
        card_rect = self.deck.top_card().rect
        card_width, card_height = card_rect.width, card.rect.height
        left_margin, top_margin = 10, 250
        hand_top_margin = top_margin + card_rect.height + 30

        self.home_pile.move_to(left_margin, top_margin)
        self.stock_pile.move_to(left_margin + card_width * 2, hand_top_margin)
        self.discard_pile.move_to(left_margin + card_width * 2  + card_width * 1.5, hand_top_margin)
        self.hand_location = CardLocation(left_margin + card_width * 2 + card_width * 1.5 * 2, hand_top_margin, card_width, card_height)
        self.cell_cards.move_to(left_margin + card_width * 2, top_margin, card_width * 1.5)

        # Move cards to their proper locations
        self.home_pile.calibrate()
        self.cell_cards.calibrate()
        self.stock_pile.calibrate()

        self.drawables = [self.home_pile, self.cell_cards, self.stock_pile, self.discard_pile]

        self.xxxcount = 0

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                card = self.deck.get_card(event.pos[0], event.pos[1])
                if card:
                    if self.home_pile.has(card) or \
                       self.discard_pile_location.has(card) or \
                       self.cell_cards.has(card):
                        self.selected_card = card

            elif event.button == 3:
                # Shuffle from stock_pile to discard_pile
                # Place in hand if count < 3,
                # otherwise place in discard pile, count = 0
                if self.xxxcount != 0 and self.stock_pile.cards.empty():
                    self.xxxcount = 3

                self.xxxcount += 1
                if self.xxxcount == 4:
                    self.discard_pile.calibrate()
                    self.xxxcount = 0
                else:
                    if self.stock_pile.cards.empty():
                        self.stock_pile.take_from(self.discard_pile.cards)
                        self.stock_pile.calibrate()

                    self.discard_pile.take_from(self.stock_pile)
                    card = self.discard_pile.cards.top_card()
                    card.rect.x = self.hand_location.rect.x + self.xxxcount * 40 

    def get_selected_card(self):
        return self.selected_card

# TODO Implement StockPile->DiscardPile abstraction
