#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame

class CardImages:
    """ Loads the card images and allows easy access to them. """

    def __init__(self):
        self.card_images = {}

        numbers = ['0', 'a', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                   'j', 'q', 'k']
        suits = ['c', 'd', 'h', 's']

        image_dir = "images"

        for i in range(52):
            num = i / 4 + 1
            suit = i % 4
            image_name = "%s/%s%s.png" % (image_dir, numbers[num], suits[suit])
            self.card_images[(num, suit)] = \
                pygame.image.load(image_name).convert()

        self.back_image = pygame.image.load("%s/back_blue.png" % image_dir)

    def images(self):
        for (number, suit), image in self.card_images.iteritems():
            yield (number, suit, image)

    def get_back(self):
        return self.back_image
