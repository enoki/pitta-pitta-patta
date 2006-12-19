#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
import sys
from PlayingField import PlayingField

class Game:
    def __init__(self):
        self.game_over = False

    def end_game(self):
        self.game_over = True

    def main(self):
        """ Pitta-pitta-patta game. """

        pygame.init()

        screen = pygame.display.set_mode((640, 768))

        pygame.display.set_caption('Pitta Pitta Patta')

        playing_field = PlayingField()

        louie.connect(self.end_game, PlayingField.game_over)

        while True:
            pygame.time.wait(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

                if not self.game_over:
                    playing_field.handle(event)

            if not self.game_over:
                playing_field.update()

            screen.fill((0x00, 0xb0, 0x00))

            playing_field.draw(screen)

            pygame.display.flip()

def main():
    game = Game()
    game.main()

if __name__ == '__main__':
    main()
