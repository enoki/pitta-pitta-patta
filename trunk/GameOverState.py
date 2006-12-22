#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Color import Color
from State import State

class GameOverState(State):
    """ The state shown after a game ends. """

    new_game = louie.Signal()

    def __init__(self, playing_field):
        self.playing_field = playing_field

    def delay(self):
        pass

    def handle(self, event):
        pass

    def update(self):
        pass

    def clear_surface(self, surface):
        pass

    def draw(self, surface):
        pass
