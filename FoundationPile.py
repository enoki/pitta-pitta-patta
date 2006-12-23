#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from Pile import Pile

class SharedImages:
    """ Private class to store shared images. """
    ghost_image = None

class FoundationPile(Pile):
    """ A pile on which players drop ordered cards. """

    def __init__(self):
        Pile.__init__(self)
        self.ghost_image = self.get_ghost_image()
        self.ghost_image_rect = self.ghost_image.get_rect()

    def get_ghost_image(self):
        if SharedImages.ghost_image is None:
            SharedImages.ghost_image = pygame.image.load('images/ghost.png')
        return SharedImages.ghost_image

    def calibrate(self):
        Pile.calibrate(self)
        self.top_card().face_up()

    def draw(self, surface):
        if self.cards.num_cards() < 2:
            self.ghost_image_rect.topleft = self.location.position()
            surface.blit(self.ghost_image, self.ghost_image_rect)

        Pile.draw(self, surface)
