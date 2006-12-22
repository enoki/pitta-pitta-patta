#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
import sys
from StartState import StartState
from PlayState import PlayState
from GameOverState import GameOverState
from PlayingField import PlayingField


class Application:
    """ Entry point to the Pitta Pitta Patta application. """

    def __init__(self):
        pygame.init()
        self.init_display()
        self.init_playing_field()
        self.init_states()
        self.connect()

    def init_display(self):
        self.set_resolution(2) 
        caption = 'Pitta Pitta Patta'
        pygame.display.set_caption(caption)

    def set_resolution(self, num_players):
        if num_players < 2 or num_players > 4:
            return

        resolutions = [(430, 660), (850, 660), (850, 660), (850, 660)]
        resolution = resolutions[num_players-2]
        display_flags = pygame.HWSURFACE | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(resolution, display_flags)

    def init_playing_field(self):
        self.playing_field = PlayingField()
        louie.connect(self.goto_game_over, PlayingField.game_over)

    def init_states(self):
        self.states = { 'start' : StartState(self.playing_field),
                        'play' : PlayState(self.playing_field),
                        'game_over' : GameOverState(self.playing_field) }
        self.state = self.states['start']

    def connect(self):
        louie.connect(self.goto_play, StartState.finished)

    def transition(self, state_name):
        self.state.exited()
        self.state = self.states[state_name]
        self.state.entered()

    def goto_game_over(self):
        self.transition('game_over')

    def goto_play(self, game_config):
        self.transition('play')
        self.playing_field.configure(game_config)
        self.set_resolution(game_config.num_players)

    def restart(self):
        """ Start a new game. deprecated? """
        self.init_states()
        self.transition('play')

    def main(self):
        """ Main application loop """

        while True:
            self.state.delay()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

                self.state.handle(event)

            self.state.update()
            self.state.clear_surface(self.screen)
            self.state.draw(self.screen)
            pygame.display.flip()

