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
