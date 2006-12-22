#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Color import Color
from GameConfig import GameConfig
from State import State

class StartState(State):
    """ The first screen players see. """

    # Sends (game_config=GameConfig()) as argument
    finished = louie.Signal() 

    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.game_config = GameConfig()

    def delay(self):
        pygame.time.wait(100)

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            louie.send(StartState.finished, game_config=self.game_config)
            pass

    def update(self):
        pass

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        pass
