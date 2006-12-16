import pygame
from Deck import Deck
from CardGroup import CardGroup
from CardLocation import CardLocation

class Player:
    def __init__(self):
        self.deck = Deck()

        self.home_pile = CardGroup()
        self.cell_cards = CardGroup()
        self.stock_pile = CardGroup()
        self.discard_pile = CardGroup()

        card_rect = self.deck.top_card().rect
        card_width = card_rect.width
        card_height = card_rect.height
        left_margin = 10
        top_margin = 250
        hand_top_margin = top_margin + card_rect.height + 30

        self.num_cell_cards = 3
        self.num_home_pile_cards = 13

        #
        self.home_pile_location = CardLocation(left_margin, top_margin, card_width, card_height)
        self.cell_cards_location = []
        x = left_margin + card_width * 2
        for i in range(self.num_cell_cards):
            self.cell_cards_location.append(CardLocation(x, top_margin, card_width, card_height))
            x += card_width * 1.5
        self.stock_pile_location = CardLocation(left_margin + card_width * 2, hand_top_margin, card_width, card_height)
        self.discard_pile_location = CardLocation(left_margin + card_width * 2 + card_width * 1.5, hand_top_margin, card_width, card_height)
        self.hand_location = CardLocation(left_margin + card_width * 2 + card_width * 1.5 * 2, hand_top_margin, card_width, card_height)

        # This may need to be more global...
        self.selected_card = None

        for i in range(self.num_home_pile_cards):
            self.home_pile.add_card(self.deck.take_top_card())

        for i in range(self.num_cell_cards):
            self.cell_cards.add_card(self.deck.take_top_card())

        for i in range(52-self.num_home_pile_cards-self.num_cell_cards):
            self.stock_pile.add_card(self.deck.take_top_card())

        for card in self.home_pile.all_cards():
            self.deck.add_card(card)
        for card in self.cell_cards.all_cards():
            self.deck.add_card(card)
        for card in self.stock_pile.all_cards():
            self.deck.add_card(card)

        # Move cards to their proper locations
        self.home_pile_location.grab_cards(self.home_pile.all_cards())
        for i in range(self.num_cell_cards):
            self.cell_cards_location[i].grab_card(self.cell_cards[i])
            self.cell_cards[i].flip()
        self.stock_pile_location.grab_cards(self.stock_pile.all_cards())

        self.home_pile.top_card().flip()

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
                    if self.home_pile_location.has(card) or \
                       self.discard_pile_location.has(card):
                        self.selected_card = card

                    for location in self.cell_cards_location:
                        if location.has(card):
                            self.selected_card = card
            elif event.button == 3:
                # Shuffle from stock_pile to discard_pile
                # Place in hand if count < 3,
                # otherwise place in discard pile, count = 0
                if self.xxxcount != 0 and self.stock_pile.empty():
                    self.xxxcount = 3

                self.xxxcount += 1
                if self.xxxcount == 4:
                    self.discard_pile.top_card().flip()
                    self.discard_pile_location.grab_cards(self.discard_pile.all_cards())
                    self.xxxcount = 0
                else:
                    if self.stock_pile.empty():
                        while not self.discard_pile.empty():
                            card = self.discard_pile.take_top_card()
                            card.backSide()
                            self.stock_pile.add_card(card)

                        self.stock_pile_location.grab_cards(self.stock_pile.all_cards())

                    card = self.stock_pile.take_top_card()
                    self.discard_pile.add_card(card)
                    card.rect.x = self.hand_location.rect.x + self.xxxcount * 40 

    def get_selected_card(self):
        return self.selected_card

# TODO Implement CellCards abstraction...
# TODO Implement StockPile->DiscardPile abstraction
