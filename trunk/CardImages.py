#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame

class CardImages:
    """ Loads the card images and allows easy access to them. """

    def __init__(self):
        self.card_images = []

        image_dir = "images"

        for i in range(52):
            image_name = "%s/%s.png" % (image_dir, i+1)
            self.card_images.append(pygame.image.load(image_name).convert())

        self.back_image = pygame.image.load("%s/b1fv.png" % image_dir)

    def get_card(self, i):
        return self.card_images[i]

    def get_back(self):
        return self.back_image
