#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Color import Color
from State import State

class PlayState(State):
    """ The state where players start playing games. """

    paused = louie.Signal()

    def __init__(self, playing_field):
        self.playing_field = playing_field

    def delay(self):
        pygame.time.wait(30)

    def handle(self, event):
        self.playing_field.handle(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause()

    def update(self):
        self.playing_field.update()

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        self.playing_field.draw(surface)

    def pause(self):
        louie.send(PlayState.paused)
