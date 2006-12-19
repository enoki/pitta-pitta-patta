#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame


class Selection:
    """ A selection is a card plus where the card calls home. """

    def __init__(self):
        self.is_empty = True

    def transfer_to(self, pile):
        """ Transfers the currently selected card to a pile. """
        if not self.empty():
            self.home.transfer(self.card, pile)

    def draw(self, surface):
        """ Draws a box around the selected card. """
        if not self.empty():
            pygame.draw.rect(surface, (0xff,0xff,0x00), self.rect, 3)

    def make_rectangle(self):
        """ Creates the rectangle that surrounds the selected card. """
        if not self.empty():
            self.rect = pygame.Rect(0,0,0,0)
            self.rect.x = self.card.rect.x - 2
            self.rect.width = self.card.rect.width + 4
            self.rect.y = self.card.rect.y - 2
            self.rect.height = self.card.rect.height + 4

    def empty(self):
        return self.is_empty

    def clear(self):
        " Clears the selection "
        self.is_empty = True

    def set(self, card, home):
        """ Changes the selection to include the card and
            the card's home. """
        self.card = card
        self.home = home
        self.is_empty = False

        self.make_rectangle()
