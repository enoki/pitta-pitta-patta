#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
import logging
import sys
from GameConfig import GameConfig
from Match import Match
from PlayingField import PlayingField
from Color import Color

def main():
    """ Simulates the playing field. """
    pygame.init()
    resolution = (850, 700)
    display_flags = pygame.HWSURFACE | pygame.DOUBLEBUF
    screen = pygame.display.set_mode(resolution, display_flags)

    match = Match()
    game_config = GameConfig()
    playing_field = PlayingField(game_config)
    playing_field.configure(match)
    for i in range(3):
        playing_field.flip_cells(i)
    a = playing_field

    logging.basicConfig(level=logging.DEBUG)
    def dump(x):
        logging.debug(x)

    def game_over():
        dump('Game over')

    louie.connect(game_over, PlayingField.game_over)

    while True:
        pygame.time.wait(30)

        for event in pygame.event.get():
            a.handle(event)

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        a.update()
        screen.fill(Color.bright_green)
        a.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
