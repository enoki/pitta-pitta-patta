#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from Pile import Pile

class FoundationPile(Pile):
    """ A pile on which players drop ordered cards. """

    def __init__(self):
        Pile.__init__(self)
        self.ghost_image = pygame.image.load('images/ghost.png')
        self.ghost_image_rect = self.ghost_image.get_rect()

    def calibrate(self):
        Pile.calibrate(self)
        self.top_card().face_up()

    def draw(self, surface):
        if self.cards.num_cards() < 2:
            self.ghost_image_rect.topleft = self.location.position()
            surface.blit(self.ghost_image, self.ghost_image_rect)

        Pile.draw(self, surface)
