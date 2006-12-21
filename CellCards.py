#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from CardCell import CardCell


class CellCards:
    """ Reserve cards taken from the Home Pile. """

    def __init__(self, home_pile):
        self.home_pile = home_pile
        self.size = 3
        self.cells = [CardCell() for i in range(self.size)]

    def set_size(self, width, height):
        """ Sets the sizes of each of the cells to be the same. """
        for cell in self.cells:
            cell.set_size(width, height)

    def move_to(self, x, y, distance_between):
        """ Moves each of the cells.
            Provide the coordinates of the leftmost cell. """

        for cell in self.cells:
            cell.move_to(x, y)
            x += distance_between

    def take_from(self, deck):
        """ Take cards from the deck. """
        for cell in self.cells:
            cell.take_from(deck)

    def calibrate(self):
        """ Prepare cards for display. """
        for cell in self.cells:
            cell.calibrate()
            cell.face_up()

    def draw(self, surface):
        """ Draws the cards. """
        for cell in self.cells:
            cell.draw(surface)

    def has(self, card):
        """ True if the card is in any of the cells. """
        for cell in self.cells:
            if cell.has(card):
                return True

        return False

    def add_card(self, card):
        """ Puts the card in an empty slot, if one exists. """
        for cell in self.cells:
            if cell.is_empty():
                cell.set_card(card)
                return

    def remove_card(self, card):
        for cell in self.cells:
            if cell.contains(card):
                cell.set_empty()
                return

    def transfer(self, card, pile):
        """ Transfers the card from here to the pile. """
        pile.add_card(card)
        self.remove_card(card)

        # replace with a card from the home pile
        if not self.home_pile.empty():
            self.home_pile.transfer(self.home_pile.top_card(), self)
            self.calibrate()

    def get_card(self, x, y):
        """ Returns the card at the specified coordinates.
            If no card is available, returns None. """
        for cell in self.cells:
            if not cell.is_empty():
                if cell.contains_point(x, y):
                    return cell.get_card()
                       
        return None

    def empty(self):
        for cell in self.cells:
            if not cell.is_empty():
                return False

        return True

    def get_available_cards(self):
        """ Returns the cards that can be moved by a player. """
        cards = []
        for cell in self.cells:
            if not cell.is_empty():
                cards.append(cell.get_card())

        return cards
