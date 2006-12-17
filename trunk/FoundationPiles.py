#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from Pile import Pile
from Selection import Selection

class FoundationPile(Pile):
    """ A pile on which players drop ordered cards. """

    def __init__(self):
        Pile.__init__(self)

    def calibrate(self):
        Pile.calibrate(self)
        self.top_card().frontSide()

    # TODO
    # Make the foundation piles actual locations:
    # X   X   X   X
    # X   X   X   X
    # 8 in total, 4 x 2

class FoundationPiles:
    """ The piles on which players drop stacks of ordered cards. """

    def __init__(self, player):
        self.rect = pygame.Rect(0, 0, 640, 250-96)
        self.piles = []
        self.player = player

    def draw(self, surface):
        for pile in self.piles:
            pile.draw(surface)

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.handle_left_mouse_down(event)

    def handle_left_mouse_down(self, event):
        (x, y) = (event.pos[0], event.pos[1])

        if not self.rect.collidepoint(x, y):
            return

        if self.player.has_selection():
            selection = self.player.get_selection()
            self.player.clear_selection()

            for pile in self.piles:
                if pile.contains(x, y):
                    if self.is_next(selection.card, pile):
                        selection.transfer_to(pile)
                        pile.calibrate()
                    return

            if self.is_starter(selection.card): # is an ace? FIXME
                self.create_pile(selection, x, y)

    def create_pile(self, selection, x, y):
        new_pile = FoundationPile()
        selection.transfer_to(new_pile)
        new_pile.move_to(x, y)
        new_pile.calibrate()
        self.piles.append(new_pile)

    def is_starter(self, card):
        """ True if the card can start a new foundation pile. """
        # TODO
        return True

    def is_next(self, card, pile):
        """ True if the card can be put on top of the foundation pile. """
        top_card = pile.top_card()
        # TODO
        return True
