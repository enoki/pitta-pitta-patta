#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from GameOverScreen import GameOverScreen
from Color import Color
from State import State

class GameOverState(State):
    """ The state shown after a game ends. """

    new_game = louie.Signal()
    escape_pressed = louie.Signal()

    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.screen = GameOverScreen()
        self.screen.create_ui(self.playing_field.game_score_summary(),
                              self.playing_field.set_score_summary())

        louie.connect(self.new_game, GameOverScreen.new_game)
        louie.connect(self.escape_pressed, GameOverScreen.escape_pressed)

        self.drawables = [self.playing_field, self.screen]
        self.handlers = [self.screen]
        self.updateables = [self.screen]

    def delay(self):
        pygame.time.wait(100)

    def handle(self, event):
        for handler in self.handlers:
            handler.handle(event)

    def update(self):
        for updateable in self.updateables:
            updateable.update()

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def new_game(self):
        louie.send(GameOverState.new_game)

    def escape_pressed(self):
        louie.send(GameOverState.escape_pressed)
