#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from Pile import Pile
from Selection import Selection
import logging

class FoundationPile(Pile):
    """ A pile on which players drop ordered cards. """

    def __init__(self):
        Pile.__init__(self)

    def calibrate(self):
        Pile.calibrate(self)
        self.top_card().face_up()

    def draw(self, surface):
        Pile.draw(self, surface)
        if self.empty():
            pygame.draw.rect(surface, (0x00,0x00,0xff), self.location.rect, 3)

class FoundationPiles:
    """ The piles on which players drop stacks of ordered cards. """

    def __init__(self, player, rules):
        """ The piles are arranged in a 2x4 grid like so:
            X  X  X  X
            X  X  X  X
        """
        self.num_piles = 8
        self.piles = [FoundationPile() for i in range(self.num_piles)]
        self.player = player
        self.rules = rules

        self.set_locations()

        self.rect = pygame.Rect(0, 250, 640, 250)

    def set_locations(self):
        """ Sets the foundation pile locations. """
        card_width = 72
        card_height = 96

        num_cols = 4
        col_width = 1.5
        total_col_width = num_cols * col_width
        row_height = 1.1

        col = 0
        row = 0

        for pile in self.piles:
            pile.set_size(card_width, card_height)
            pile.move_to(col * card_width + card_width * 0.25,
                         row * card_height + card_height * 0.25 + 250)
            col += col_width
            if col == total_col_width:
                col = 0
                row += row_height

    def draw(self, surface):
        for pile in self.piles:
            pile.draw(surface)

    def update(self):
        pass

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

            for pile in self.piles:
                if pile.contains(x, y):
                    logging.warning('move "' + str(selection.card) + '"?')
                    if self.rules.is_valid(selection.card, pile):
                        selection.transfer_to(pile)
                        pile.calibrate()
                        self.player.inc_score()
                    self.player.clear_selection()
                    return

            self.player.clear_selection()
