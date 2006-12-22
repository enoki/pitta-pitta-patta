#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Button import Button
from Color import Color
from Label import Label
from RectContainer import RectContainer
from State import State

class GameOverState(State):
    """ The state shown after a game ends. """

    new_game = louie.Signal()

    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.informative = False

        self.font = pygame.font.SysFont("Arial", 24)
        self.label = Label(self.font, Color.white, Color.medium_blue)
        self.main_widget = RectContainer(Color.medium_blue)

        self.drawables = []
        self.handlers = []

    def delay(self):
        pygame.time.wait(100)

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.toggle_informative()
            elif event.key == pygame.K_RETURN:
                self.new_game()

        for handler in self.handlers:
            handler.handle(event)

    def update(self):
        if self.label.empty():
            self.create_ui()

    def create_ui(self):
        self.label.set_text(self.create_label_text())

        new_game_button = self.make_button('Click to start a new game (Enter)')
        louie.connect(self.new_game, Button.clicked, new_game_button)

        informative_button = self.make_button(self.create_informative_button_text())
        louie.connect(self.toggle_informative, Button.clicked, informative_button)

        main_widget_children = [self.label, new_game_button, informative_button]
        self.main_widget.create_ui(main_widget_children)

        self.drawables = [self.playing_field, self.main_widget]
        self.handlers = [self.main_widget]

    def create_label_text(self):
        """ Returns the text in the label. """
        text = 'Game over\n'
        text += '\n'

        winner = self.playing_field.get_winner()
        if not winner:
            return

        if winner == self.playing_field.player:
            text += 'You Win!\n'
        else:
            text += winner.get_name() + ' Wins!\n'
        text += '\n'

        for player in self.playing_field.players:
            score = player.get_score()
            name = player.get_name()

            text += name + ': ' + str(score)

            if self.informative:
                num_good = player.num_good_cards()
                num_bad = player.num_bad_cards()

                text += '     (' + str(score) + ' = ' + \
                        str(num_good) + ' - ' + str(num_bad) + 'x2)'

            text += '\n'

        return text

    def create_informative_button_text(self):
        """ Creates the text for the informative? button """
        text = 'Click for '
        if self.informative:
            text += 'less '
        else:
            text += 'more '
        text += 'information (Spacebar)'
        return text

    def make_button(self, text):
        return Button(self.font,
                      Color.white, Color.medium_blue, Color.dark_blue,
                      0, text)

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def toggle_informative(self):
        self.informative = not self.informative
        self.create_ui()

    def new_game(self):
        louie.send(GameOverState.new_game)
