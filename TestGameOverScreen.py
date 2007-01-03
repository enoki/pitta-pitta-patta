#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
import logging
import sys
from GameOverScreen import GameOverScreen
from Color import Color

def main():
    """ Tests just the game over screen. """
    pygame.init()
    screen = pygame.display.set_mode((430, 660), pygame.HWSURFACE | pygame.DOUBLEBUF)

    game_data = [['Grant', '3',  '-5', '3', '10'],
                 ['Ally',  '4',  '-2', '2', '12'],
                 ['Bob',   '10', '-2', '8', '15'],
                 ['Sue',   '11', '-4', '7', '35']]

    set_data = [['Grant', '3',  '5', '3', '', '', '', '10'],
                ['Ally',  '4',  '2', '2', '', '', '', '12'],
                ['Bob',   '10', '2', '8', '', '', '', '15'],
                ['Sue',   '11', '4', '7', '', '', '', '35']]

    a = GameOverScreen()
    a.create_ui(game_data, set_data)

    logging.basicConfig(level=logging.DEBUG)
    def dump(x):
        logging.debug(x)

    def new_game():
        dump('New game')

    def escape_pressed():
        dump('Escape pressed')

    louie.connect(new_game, GameOverScreen.new_game)
    louie.connect(escape_pressed, GameOverScreen.escape_pressed)

    while True:
        pygame.time.wait(100)

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
