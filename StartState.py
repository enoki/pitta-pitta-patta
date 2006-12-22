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
        label.set_y(180)
        
        two_p_button = self.make_button('2 Players')
        three_p_button = self.make_button('3 Players')
        four_p_button = self.make_button('4 Players')

        label_spacer = self.make_label(' ')

        louie.connect(self.start2p, Button.clicked, two_p_button)
        louie.connect(self.start3p, Button.clicked, three_p_button)
        louie.connect(self.start4p, Button.clicked, four_p_button)

        children = [label, two_p_button, three_p_button, four_p_button,
                    label_spacer]
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

    def start2p(self):
        self.start_game(2)

    def start3p(self):
        self.start_game(3)

    def start4p(self):
        self.start_game(4)

    def start_game(self, num_players):
        self.game_config.num_players = num_players
        louie.send(StartState.finished, game_config=self.game_config)
