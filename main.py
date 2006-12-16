#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import sys
from Deck import Deck
from CardDraggingEventHandler import CardDraggingEventHandler

def main():
    """ Pitta-pitta-patta game. """

    pygame.init()

    screen = pygame.display.set_mode((640, 480))

    pygame.display.set_caption('Pitta Pitta Patta')

    deck = Deck()
    handler = CardDraggingEventHandler(deck)

    while True:
        pygame.time.wait(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            else:
                handler.handle_card_dragging(event)

        screen.fill((0x00, 0xb0, 0x00))

        deck.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
