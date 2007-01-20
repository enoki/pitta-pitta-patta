#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
import sys
from StartState import StartState
from OptionsState import OptionsState
from PrepareState import PrepareState
from PlayState import PlayState
from PausedState import PausedState
from GameOverState import GameOverState
from PlayingField import PlayingField
from GameConfig import GameConfig


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

        resolutions = [(430, 700), (850, 700), (850, 700), (850, 700)]
        resolution = resolutions[num_players-2]
        display_flags = pygame.HWSURFACE | pygame.DOUBLEBUF
        self.screen = pygame.display.set_mode(resolution, display_flags)

    def init_playing_field(self):
        self.playing_field = PlayingField()
        louie.connect(self.goto_game_over, PlayingField.game_over)

    def config_playing_field(self, game_config):
        if game_config.dirty:
            game_config.dirty = False
            self.playing_field.configure(game_config)
            self.set_resolution(game_config.num_players)
            self.next_game_config = game_config # FIXME

    def init_states(self):
        self.states = { 'start' : StartState(self.playing_field),
                        'options' : OptionsState(self.playing_field),
                        'prepare' : PrepareState(self.playing_field),
                        'play' : PlayState(self.playing_field),
                        'paused' : PausedState(self.playing_field),
                        'game_over' : None }
        self.state = self.states['start']
        self.config_playing_field(self.states['options'].game_config)

    def connect(self):
        louie.connect(self.goto_prepare, StartState.finished)
        louie.connect(self.goto_options, StartState.options)
        louie.connect(self.goto_start, OptionsState.finished)
        louie.connect(self.goto_play, PrepareState.finished)
        louie.connect(self.goto_play, PausedState.finished)
        louie.connect(self.goto_paused, PlayState.paused)
        louie.connect(self.goto_paused, PrepareState.paused)
        louie.connect(self.restart, GameOverState.new_game)
        louie.connect(self.return_to_start, GameOverState.escape_pressed)

    def transition(self, state_name):
        self.state.exited()
        self.state = self.states[state_name]
        self.state.entered()

    def reset_state(self, state_name, new_state):
        self.states[state_name] = new_state

    def goto_game_over(self):
        self.reset_state('game_over', GameOverState(self.playing_field))
        self.transition('game_over')

    def return_to_start(self):
        self.transition('start')

    def goto_start(self, game_config):
        self.config_playing_field(game_config)
        self.transition('start')
        self.state.game_config = game_config

    def goto_options(self):
        self.transition('options')

    def goto_prepare(self, game_config):
        self.config_playing_field(game_config)
        self.transition('prepare')
        self.state.configure(game_config)

    def goto_play(self):
        self.transition('play')

    def goto_paused(self):
        self.transition('paused')

    def restart(self):
        """ Start a new game. deprecated? """
        self.playing_field.configure(self.next_game_config)
        self.transition('prepare')

    def main(self):
        """ Main application loop """

        while True:
            self.state.delay()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F4:
                        if pygame.key.get_mods() and pygame.KMOD_ALT:
                            sys.exit()

                self.state.handle(event)

            self.state.update()
            self.state.clear_surface(self.screen)
            self.state.draw(self.screen)
            pygame.display.flip()

