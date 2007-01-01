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

    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.num_ticks = 4
        self.time_to_tick = 500
        self.tick_count = 0
        self.last_tick = pygame.time.get_ticks()
        self.font = pygame.font.SysFont("Arial", 36)
        self.label = Label(self.font, Color.white, Color.medium_blue)

    def entered(self):
        self.tick_count = 0
        self.last_tick = pygame.time.get_ticks()
        self.label.set_text(self.create_round_text(1))

    def delay(self):
        pygame.time.wait(30)

    def handle(self, event):
        pass

    def update(self):
        if self.label.empty():
            self.label.set_text(self.create_round_text(1))

        if pygame.time.get_ticks() - self.last_tick > self.time_to_tick:
            self.last_tick = pygame.time.get_ticks()
            self.tick_count += 1

            if self.tick_count == self.num_ticks+1:
                louie.send(PrepareState.finished)

            if self.tick_count == self.num_ticks:
                self.label.set_text(self.create_round_text('Start!'))
            else:
                self.label.set_text(self.create_round_text(self.tick_count))

    def create_round_text(self, number):
        text = 'Round 1: '
        text += self.playing_field.get_round_name()
        text += '\n'
        text += str(number)
        return text

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        self.playing_field.draw(surface)
        self.label.center_vertically_on(surface)
        self.label.draw(surface)
