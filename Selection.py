#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame


class EmptySelection:
    """ An empty selection. """

    def __init__(self):
        pass

    def draw(self, surface):
        pass

    def empty(self):
        return True


class Selection:
    """ A selection is a card plus where the card calls home. """

    def __init__(self, card, home):
        self.card = card
        self.home = home

        self.make_rectangle()

    def transfer_to(self, pile):
        self.home.transfer(self.card, pile)

    def draw(self, surface):
        pygame.draw.rect(surface, (0xff,0xff,0x00), self.rect, 3)

    def make_rectangle(self):
        self.rect = pygame.Rect(0,0,0,0)
        self.rect.x = self.card.rect.x - 2
        self.rect.width = self.card.rect.width + 4
        self.rect.y = self.card.rect.y - 2
        self.rect.height = self.card.rect.height + 4

    def empty(self):
        return False
