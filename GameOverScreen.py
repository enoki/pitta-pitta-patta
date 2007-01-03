#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
import Table
from Button import Button
from Color import Color
from Label import Label
from RectContainer import RectContainer


class GameOverScreen:
    """ The screen shown after a game ends. """

    new_game = louie.Signal()
    escape_pressed = louie.Signal()

    def __init__(self):
        self.title_font = pygame.font.SysFont("Arial", 24)
        self.font = pygame.font.SysFont("Arial", 20)
        self.main_widget = RectContainer(Color.medium_blue)

        self.drawables = []
        self.handlers = []

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.new_game()
            elif event.key == pygame.K_ESCAPE:
                louie.send(GameOverScreen.escape_pressed)

        for handler in self.handlers:
            handler.handle(event)

    def update(self):
        pass

    def create_ui(self, game_score_summary, set_score_summary):
        title_label = self.make_label('Stats\n', self.title_font)
        spacer = self.make_label(' ')
        spacer0 = self.make_label(' ')
        game_box_scores = self.make_game_table(game_score_summary)
        set_box_scores = self.make_set_table(set_score_summary)

        title_label.set_y(75)

        new_game_button = self.make_button('Continue')
        louie.connect(self.new_game, Button.clicked, new_game_button)

        main_widget_children = [title_label,
                                game_box_scores, 
                                set_box_scores, 
                                new_game_button]
        self.main_widget.create_ui(main_widget_children)

        self.drawables = [self.main_widget]
        self.handlers = [self.main_widget]

    def make_label(self, text, font=None):
        if not font:
            font = self.font

        label = Label(font, Color.white, Color.medium_blue)
        label.set_text(text)
        return label

    def make_game_table(self, score_summary):
        """ Returns the box score table for the last game. """

        title = 'Game'
        data = [['Name', 'Put out', 'Subtract', 'Score', 'Total']]

        data.extend(score_summary)

        table = self.make_table(data, title)
        table.set_right_col_border(0)
        table.set_right_col_border(-2)
        table.set_bottom_row_border(0)
        return table

    def make_set_table(self, score_summary):
        """ Returns the box score table for the current set. """

        title = 'Set'
        data = [['Name', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', 'Total']]

        data.extend(score_summary)

        table = self.make_table(data, title)
        table.set_right_col_border(0)
        table.set_right_col_border(-2)
        table.set_bottom_row_border(0)
        return table

    def make_table(self, data, title):
        return Table.Table(self.font,
                           Color.white, Color.medium_blue, data, title)

    def make_button(self, text):
        return Button(self.font,
                      Color.white, Color.medium_blue, Color.dark_blue,
                      0, text)

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def new_game(self):
        louie.send(GameOverScreen.new_game)
