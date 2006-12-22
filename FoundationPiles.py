#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from FoundationPile import FoundationPile
from Selection import Selection

class FoundationPiles:
    """ The piles on which players drop stacks of ordered cards. """

    def __init__(self, player, rules, num_players):
        """ The piles are arranged in a 2x4 grid like so:
            X  X  X  X
            X  X  X  X
        """
        self.num_piles = num_players * 4
        self.piles = [FoundationPile() for i in range(self.num_piles)]
        self.player = player
        self.rules = rules

        self.set_locations()

        # anyplace besides the player's cards
        # should take into account top_margin of player
        self.rect = pygame.Rect(0, 0, 850, 450)

    def set_locations(self):
        """ Sets the foundation pile locations. """
        card_width = 72
        card_height = 96

        assert(self.num_piles % 2 == 0)
        num_cols = self.num_piles / 2
        col_width = 1.37
        total_col_width = num_cols * col_width
        row_height = 1.1

        col = 0
        row = 0

        for pile in self.piles:
            pile.set_size(card_width, card_height)
            pile.move_to(col * card_width + card_width * 0.25,
                         row * card_height + card_height * 0.25 + 200)
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
                    if self.rules.is_valid(selection.card, pile):
                        selection.transfer_to(pile)
                        self.player.inc_score()
                    self.player.clear_selection()
                    return

            self.player.clear_selection()
