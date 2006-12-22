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

    def calibrate(self):
        Pile.calibrate(self)
        self.top_card().face_up()

    def draw(self, surface):
        Pile.draw(self, surface)
        # Draw ugly blue rectangle
        # TODO replace with a pretty image
        if self.empty():
            pygame.draw.rect(surface, (0x00,0x00,0xff), self.location.rect, 3)

