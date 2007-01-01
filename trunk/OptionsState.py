#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Button import Button
from ButtonGroup import ButtonGroup
from Color import Color
from GameConfig import GameConfig
from Label import Label
from RectContainer import RectContainer
from State import State
from SkillLevels import *

class OptionsState(State):
    """ The first screen players see. """

    # Sends (game_config=GameConfig()) as argument
    finished = louie.Signal() 

    def __init__(self):
        self.game_config = GameConfig()
        self.widget = RectContainer(Color.medium_blue)
        self.font = pygame.font.SysFont("Arial", 16)
        self.nump_buttons = ButtonGroup()
        self.skill_buttons = ButtonGroup()

    def delay(self):
        pygame.time.wait(100)

    def handle(self, event):
        self.widget.handle(event)

    def update(self):
        if self.widget.empty():
            self.create_ui()

    def create_ui(self):
        label = self.make_label('\nPitta Pitta Patta Options\n')
        label.set_y(100)
        
        two_p_button = self.make_button('2 Players')
        three_p_button = self.make_button('3 Players')
        four_p_button = self.make_button('4 Players')

        label_spacer = self.make_label(' ')
        label_spacer0 = self.make_label(' ')
        label_spacer1 = self.make_label(' ')

        easy_button = self.make_button('Easy')
        normal_button = self.make_button('Normal')
        hard_button = self.make_button('Hard')

        finished_button = self.make_button('Finished')

        louie.connect(self.set_2p, Button.clicked, two_p_button)
        louie.connect(self.set_3p, Button.clicked, three_p_button)
        louie.connect(self.set_4p, Button.clicked, four_p_button)
        louie.connect(self.set_easy, Button.clicked, easy_button)
        louie.connect(self.set_normal, Button.clicked, normal_button)
        louie.connect(self.set_hard, Button.clicked, hard_button)
        louie.connect(self.finish_up, Button.clicked, finished_button)

        nump_buttons = [two_p_button, three_p_button, four_p_button]
        self.nump_buttons.set_buttons(nump_buttons)
        self.nump_buttons.set_check_color(Color.white)

        skill_buttons = [easy_button, normal_button, hard_button]
        self.skill_buttons.set_buttons(skill_buttons)
        self.skill_buttons.set_check_color(Color.white)

        nump_buttons[self.game_config.num_players-2].set_checked(True)
        skill_buttons[1].set_checked(True)

        children = [label, two_p_button, three_p_button, four_p_button,
                    label_spacer1,
                    easy_button, normal_button, hard_button,
                    label_spacer, finished_button, label_spacer0]
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

    def set_2p(self):
        self.set_nump(2)

    def set_3p(self):
        self.set_nump(3)

    def set_4p(self):
        self.set_nump(4)

    def set_easy(self):
        self.set_skill(EasySkillLevel())

    def set_normal(self):
        self.set_skill(NormalSkillLevel())

    def set_hard(self):
        self.set_skill(HardSkillLevel())

    def finish_up(self):
        louie.send(OptionsState.finished, game_config=self.game_config)

    def set_nump(self, num_players):
        self.game_config.num_players = num_players

    def set_skill(self, skill):
        self.game_config.computer_skill = skill
