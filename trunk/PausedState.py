#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Color import Color
from State import State
from Label import Label

class PausedState(State):
    """ The state where the game is paused. """

    finished = louie.Signal()

    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.font = pygame.font.SysFont("Arial", 36)
        self.label = Label(self.font, Color.white, Color.medium_blue)

    def delay(self):
        pygame.time.wait(30)

    def handle(self, event):
        pass

    def entered(self):
        if self.label.empty():
            self.label.set_text('Paused\nPress escape to resume')

    def update(self):
        pass

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        self.playing_field.draw(surface)
        self.label.center_vertically_on(surface)
        self.label.draw(surface)

    def finish(self):
        louie.send(PausedState.finished)
