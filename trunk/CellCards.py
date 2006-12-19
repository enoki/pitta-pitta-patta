#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from CardGroup import CardGroup
from CardLocation import CardLocation


class CellCards:
    """ Reserve cards taken from the Home Pile. """

    def __init__(self, home_pile):
        self.cards = CardGroup()
        self.locations = []
        self.home_pile = home_pile
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
            self.cards[i].face_up()
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

    def add_card(self, card):
        self.cards.add_card(card)

    def transfer(self, card, pile):
        """ Transfers the card from here to the pile. """
        pile.add_card(card)
        self.cards.cards.remove(card)

        # replace with a card from the home pile
        if not self.home_pile.empty():
            self.home_pile.transfer(self.home_pile.top_card(), self)
            self.calibrate()

    def get_card(self, x, y):
        """ Returns the card at the specified coordinates.
            If no card is available, returns None. """
        return self.cards.get_card(x, y)
