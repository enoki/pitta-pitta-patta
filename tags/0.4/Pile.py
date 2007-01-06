#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from CardGroup import CardGroup
from CardLocation import CardLocation

class Pile:
    """ A pile of cards. """

    def __init__(self):
        self.cards = CardGroup()
        self.location = CardLocation()

    def set_size(self, width, height):
        """ Sets the size of each card in the pile. """
        self.location.rect.width = width
        self.location.rect.height = height

    def move_to(self, x, y):
        """ Moves the pile to a different location. """
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

    def has(self, card):
        """ True if the card is located on this pile. """
        return self.location.has(card)

    def contains(self, x, y):
        return self.location.contains(x, y)

    def top_card(self):
        return self.cards.top_card()

    def add_card(self, card):
        self.cards.add_card(card)

    def remove_card(self, card):
        self.cards.cards.remove(card)

    def transfer(self, card, pile):
        """ Transfers the card from here to the pile. """
        card.throw_to(pile)
        self.remove_card(card)

    def empty(self):
        return self.cards.empty()

    def get_card(self, x, y):
        """ Returns the top card at the specified coordinates.
            If no card is available, returns None. """
        if not self.empty():
            card = self.top_card()
            if card.rect.collidepoint(x, y):
                return card

        return None

    def draw(self, surface):
        """ Draws the pile. """
        for card in self.cards.all_cards():
            card.draw(surface)

    def get_available_cards(self):
        """ Returns the cards that can be moved by a player. """
        cards = []
        if not self.empty():
            cards.append(self.top_card())

        return cards

    def position(self):
        return self.location.position()
