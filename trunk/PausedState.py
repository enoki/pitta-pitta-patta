#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
import sys
from Button import Button
from Color import Color
from RectContainer import RectContainer
from State import State
from Label import Label

class PausedState(State):
    """ The state where the game is paused. """

    finished = louie.Signal()

    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.title_font = pygame.font.SysFont("Arial", 36)
        self.button_font = pygame.font.SysFont("Arial", 24)
        self.widget = RectContainer(Color.medium_blue)

    def delay(self):
        pygame.time.wait(30)

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.finish()
            elif event.key == pygame.K_RETURN:
                sys.exit()

        self.widget.handle(event)

    def create_ui(self):
        label = Label(self.title_font, Color.white, Color.medium_blue)
        label.set_text('Paused')
        label.set_y(200)

        a, b = self.make_spacer(), self.make_spacer()
        
        resume_button = self.make_button('Resume (Escape)')
        exit_button = self.make_button('Exit Game')

        louie.connect(self.finish, Button.clicked, resume_button)
        louie.connect(self.exit, Button.clicked, exit_button)

        self.widget.create_ui([label, a, resume_button, exit_button, b])

    def make_spacer(self):
        spacer = Label(self.button_font, Color.white, Color.medium_blue)
        spacer.set_text(' ')
        return spacer

    def make_button(self, text):
        return Button(self.button_font,
                      Color.white, Color.medium_blue, Color.dark_blue,
                      0, text)

    def entered(self):
        if self.widget.empty():
            self.create_ui()

    def update(self):
        pass

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        self.playing_field.draw(surface)
        self.widget.draw(surface)

    def finish(self):
        louie.send(PausedState.finished)

    def exit(self):
        sys.exit()
