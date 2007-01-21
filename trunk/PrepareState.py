#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Color import Color
from Label import Label
from State import State

class PrepareState(State):
    """ The state where players are shown a message to get ready to play. """

    finished = louie.Signal()
    paused = louie.Signal()

    def __init__(self, playing_field, game_config):
        self.playing_field = playing_field
        self.game_config = game_config
        self.time_to_tick = 200
        self.tick_count = 0
        self.is_paused = False
        self.last_tick = pygame.time.get_ticks()
        self.font = pygame.font.SysFont("Arial", 36)

    def entered(self):
        self.tick_count = 0
        self.last_tick = pygame.time.get_ticks()
        self.num_ticks = 3 #self.game_config.num_cells

    def delay(self):
        pygame.time.wait(30)

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.pause()

    def update(self):
        if self.is_paused:
            return

        if pygame.time.get_ticks() - self.last_tick > self.time_to_tick:
            self.last_tick = pygame.time.get_ticks()

            if self.tick_count == self.num_ticks-1:
                louie.send(PrepareState.finished)

            self.playing_field.flip_cells(self.tick_count)

            self.tick_count += 1


    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        self.playing_field.draw(surface)

    def pause(self):
        louie.send(PrepareState.paused)
