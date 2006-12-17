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

    def contains(self, x, y):
        return self.location.contains(x, y)

    def top_card(self):
        return self.cards.top_card()

    def add_card(self, card):
        self.cards.add_card(card)

    def transfer(self, card, pile):
        pile.add_card(card)
        self.cards.cards.remove(card)

    def empty(self):
        return self.cards.empty()
