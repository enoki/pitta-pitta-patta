#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from CardGroup import CardGroup
from CardLocation import CardLocation


class RightHand:
    """ Reserve cards from the Stock Pile held in the right hand. """

    def __init__(self):
        self.cards = CardGroup()
        self.locations = []
        self.size = 3

    def set_size(self, width, height):
        """ Sets the sizes of each of the cells to be the same. """
        for location in self.locations:
            location.rect.width = width
            location.rect.height = height

    def move_to(self, x, y, distance_between):
        """ Moves each of the cells.
            Provide the coordinates of the leftmost cell. """

        for i in range(self.size):
            location = CardLocation()
            location.rect.x = x
            self.locations.append(location)

            x += distance_between

        for location in self.locations:
            location.rect.y = y

    def take_from(self, stock_pile):
        """ Take the top card from the stock pile. """
        self.cards.add_card(stock_pile.take_top_card())

    def calibrate(self):
        """ Prepare cards for display. """
        # Move all cards to the HomePile location.
        for i in range(self.cards.num_cards()):
            self.locations[i].grab_card(self.cards[i])
            self.cards[i].backSide() # XXX
        self.resize()

    def resize(self):
        """ Resize to the top card. """
        card_rect = self.cards.top_card().rect
        self.set_size(card_rect.width, card_rect.height)

    def draw(self, surface):
        """ Draws the cards. """
        self.cards.draw(surface)
