#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Color import Color
from Label import Label
from State import State

class GameOverState(State):
    """ The state shown after a game ends. """

    new_game = louie.Signal()

    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.informative = False

        font = pygame.font.SysFont("Arial", 24)
        self.label = Label(font, Color.white, Color.medium_blue)

    def delay(self):
        pygame.time.wait(100)

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.toggle_informative()
            elif event.key == pygame.K_RETURN:
                self.new_game()

    def update(self):
        if self.label.empty():
            self.create_ui()

    def create_ui(self):
        text = 'Game over\n'
        text += '\n'

        winner = self.playing_field.get_winner()
        assert(winner)

        if winner in self.playing_field.players:
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

        text += '\n'
        text += 'Press enter to start a new game\n'
        text += 'Press space for '
        if self.informative:
            text += 'less '
        else:
            text += 'more '
        text += 'information\n'

        self.label.set_text(text)

    def clear_surface(self, surface):
        surface.fill(Color.bright_green)

    def draw(self, surface):
        self.playing_field.draw(surface)
        self.label.draw(surface)

    def toggle_informative(self):
        self.informative = not self.informative
        self.create_ui()

    def new_game(self):
        louie.send(GameOverState.new_game)
