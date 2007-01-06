#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from CardCell import CardCell


class RightHand:
    """ Reserve cards from the Stock Pile held in the right hand. """

    def __init__(self):
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

    def take_from(self, stock_pile):
        """ Take the top card from the stock pile. """
        for cell in self.cells:
            if cell.is_empty():
                cell.set_card(stock_pile.take_top_card())
                return

    def calibrate(self):
        """ Prepare cards for display. """
        for cell in self.cells:
            cell.calibrate()
            cell.face_down()

    def draw(self, surface):
        """ Draws the cards. """
        for cell in self.cells:
            cell.draw(surface)

    def cards(self):
        cards = []
        for cell in self.cells:
            if not cell.is_empty():
                cards.append(cell.get_card())

        return cards

    def top_card(self):
        for cell in reversed(self.cells):
            if not cell.is_empty():
                return cell.get_card()
        return None

    def rip_cards(self):
        """ Returns all the cards from the cells and removes them
            from the cells. """
        cards = []
        for cell in self.cells:
            if not cell.is_empty():
                card = cell.get_card()
                cell.set_empty()
                cards.append(card)
        return cards
