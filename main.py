#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import sys
from CardGroup import CardGroup
from Card import Card
from Deck import Deck

def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    pygame.display.set_caption('Pitta Pitta Patta')

    
    deck = Deck()

    selected_card = None

    (DEFAULT, DRAGGING) = range(2)
    mode = DEFAULT


    while True:
        #clock.tick(60)
        pygame.time.wait(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button in [1,2,3]:
                    if mode == DEFAULT:
                        selected_card = deck.get_card(event.pos[0], event.pos[1])
                        if selected_card:
                            mode = DRAGGING

                            if event.button == 3:
                                selected_card.flip()
            elif event.type == pygame.MOUSEBUTTONUP:
                if mode == DRAGGING:
                    deck.drop_card(selected_card)
                    selected_card = None
                    mode = DEFAULT
                else:
                    if event.button == 2:
                        selected_card.flip()
            elif event.type == pygame.MOUSEMOTION:
                if event.buttons[0] or event.buttons[1] or event.buttons[2]:
                    if mode == DRAGGING:
                        selected_card.move(event.rel[0], event.rel[1])

        screen.fill((0x00, 0xb0, 0x00))

        deck.draw(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main()
