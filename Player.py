import pygame
from Deck import Deck
from CardGroup import CardGroup
from CardLocation import CardLocation

class Pile:
    """ A pile of cards. """

    def __init__(self):
        self.cards = CardGroup()
        self.location = CardLocation()

    def set_size(self, width, height):
        self.location.rect.width = width
        self.location.rect.height = height

    def move_to(self, x, y):
        self.location.rect.x = x
        self.location.rect.y = y

    def calibrate(self):
        """ Prepare cards for display. """
        self.location.grab_cards(self.cards.all_cards())
        self.resize()

    def resize(self):
        """ Resize to the top card. """
        card_rect = self.cards.top_card().rect
        self.set_size(card_rect.width, card_rect.height)

    def draw(self, surface):
        """ Draws the cards in this pile. """
        self.cards.draw(surface)

    def has(self, card):
        """ True if the card is located on this pile. """
        return self.location.has(card)


class StockPile(Pile):
    """ The cards the player holds in his hand during play. """

    def __init__(self):
        Pile.__init__(self)

    def take_from(self, deck):
        """ Take all cards from the deck. Flip them over as well. """
        while not deck.empty():
            card = deck.take_top_card()
            card.backSide()
            self.cards.add_card(card)


class HomePile(Pile):
    """ The cards the player must get rid of in order to stop the game. """
    def __init__(self):
        Pile.__init__(self)
        self.initial_size = 13

    def take_from(self, deck):
        """ Take cards from the deck. Flip over the top card. """
        for i in range(self.initial_size):
            self.cards.add_card(deck.take_top_card())

        self.cards.top_card().flip()


class DiscardPile(Pile):
    """ The cards the player shuffles from their Stock Pile. """
    def __init__(self):
        Pile.__init__(self)

    def take_from(self, stock_pile):
        """ Take all cards from the deck. Flip them over as well. """
        self.cards.add_card(stock_pile.cards.take_top_card())

    def calibrate(self):
        """ Prepare cards for display. """
        self.cards.top_card().flip()
        Pile.calibrate(self)


class CellCards:
    """ Reserve cards taken from the Home Pile. """

    def __init__(self):
        self.cards = CardGroup()
        self.locations = []
        self.initial_size = 3

    def set_size(self, width, height):
        """ Sets the sizes of each of the cells to be the same. """
        for location in self.locations:
            location.rect.width = width
            location.rect.height = height

    def move_to(self, x, y, distance_between):
        """ Moves each of the cells.
            Provide the coordinates of the leftmost cell. """

        for i in range(self.initial_size):
            location = CardLocation()
            location.rect.x = x
            self.locations.append(location)

            x += distance_between

        for location in self.locations:
            location.rect.y = y

    def take_from(self, deck):
        """ Take cards from the deck. """
        for i in range(self.initial_size):
            self.cards.add_card(deck.take_top_card())

    def calibrate(self):
        """ Prepare cards for display. """
        # Move all cards to the HomePile location.
        for i in range(self.initial_size):
            self.locations[i].grab_card(self.cards[i])
            self.cards[i].flip()
        self.resize()

    def resize(self):
        """ Resize to the top card. """
        card_rect = self.cards.top_card().rect
        self.set_size(card_rect.width, card_rect.height)

    def draw(self, surface):
        """ Draws the cards. """
        self.cards.draw(surface)

    def has(self, card):
        """ True if the card is in any of the cells. """
        for location in self.locations:
            if location.has(card):
                return True

        return False

class Player:
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
