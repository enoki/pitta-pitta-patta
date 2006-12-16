#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import sys
from Player import Player

def main():
    """ Pitta-pitta-patta game. """

    pygame.init()

    screen = pygame.display.set_mode((640, 480))

    pygame.display.set_caption('Pitta Pitta Patta')

    player = Player()

    while True:
        pygame.time.wait(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

            player.handle(event)

        screen.fill((0x00, 0xb0, 0x00))

        player.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
