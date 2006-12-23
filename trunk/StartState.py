#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Button import Button
from Color import Color
from GameConfig import GameConfig
from Label import Label
from RectContainer import RectContainer
from State import State

class StartState(State):
    """ The first screen players see. """

    # Sends (game_config=GameConfig()) as argument
    finished = louie.Signal() 

    # no arguments
    options = louie.Signal()


    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.game_config = GameConfig()
        self.widget = RectContainer(Color.medium_blue)
        self.font = pygame.font.SysFont("Arial", 24)

    def delay(self):
        pygame.time.wait(100)

    def handle(self, event):
        self.widget.handle(event)

    def update(self):
        if self.widget.empty():
            self.create_ui()

    def create_ui(self):
        label = self.make_label('\nPitta Pitta Patta\n')
        label.set_y(150)
        
        label_spacer0 = self.make_label(' ')

        play_button = self.make_button('Play')
        options_button = self.make_button('Options')

        louie.connect(self.start_game, Button.clicked, play_button)
        louie.connect(self.set_options, Button.clicked, options_button)

        children = [label, play_button, options_button, 
                    label_spacer0]
        self.widget.create_ui(children)

    def make_label(self, text):
        label = Label(self.font, Color.white, Color.medium_blue)
        label.set_text(text)
        return label

    def make_button(self, text):
        return Button(self.font,
                      Color.white, Color.medium_blue, Color.dark_blue,
                      0, text)

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        self.widget.draw(surface)

    def start_game(self):
        louie.send(StartState.finished, game_config=self.game_config)

    def set_options(self):
        louie.send(StartState.options)
