#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
import sys
from PlayingField import PlayingField

class State:
    pass

class StartState(State):
    finished = louie.Signal()

    def __init__(self):
        text = 'Welcome to Pitta Pitta Patta!'

        font = pygame.font.SysFont("Arial", 36)
        self.text_image = font.render(text, 1, (10, 10, 10))

    def handle(self, event):
        if event.type == pygame.KEYDOWN or \
           event.type == pygame.MOUSEBUTTONDOWN:
            louie.send(StartState.finished)

    def update(self):
        pass

    def draw(self, surface):
        text_pos = self.text_image.get_rect(centerx=surface.get_width()/2)
        surface.blit(self.text_image, text_pos)

class PlayingState(State):  
    def __init__(self, playing_field):
        self.playing_field = playing_field

    def handle(self, event):
        self.playing_field.handle(event)

    def update(self):
        self.playing_field.update()

    def draw(self, surface):
        self.playing_field.draw(surface)

class GameOverState(State):
    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.text_image = None

    def handle(self, event):
        pass

    def update(self):
        computer_score = self.playing_field.computer.get_score()
        player_score = self.playing_field.player.get_score()

        text = 'Game over. Me: ' + str(computer_score) + \
               ' You: ' + str(player_score)

        if computer_score >= player_score:
            text += ' I Win!'
        else:
            text += ' You Win!'

        font = pygame.font.Font(None, 36)
        self.text_image = font.render(text, 1, (10, 10, 10))

    def draw(self, surface):
        self.playing_field.draw(surface)

        if self.text_image:
            text_pos = self.text_image.get_rect(centerx=surface.get_width()/2)
            surface.blit(self.text_image, text_pos)
    

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 768))

        pygame.display.set_caption('Pitta Pitta Patta')

        self.create_states()

    def create_states(self):
        playing_field = PlayingField()
        louie.connect(self.end_game, PlayingField.game_over)

        start_state = StartState()
        playing_state = PlayingState(playing_field)
        game_over_state = GameOverState(playing_field)

        louie.connect(self.start_playing, StartState.finished)

        self.states = { 'Start' : start_state,
                        'Playing' : playing_state,
                        'GameOver' : game_over_state }

        self.state = self.states['Start']

    def end_game(self):
        self.state = self.states['GameOver']

    def start_playing(self):
        self.state = self.states['Playing']

    def main(self):
        """ Pitta-pitta-patta game. """

        while True:
            pygame.time.wait(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

                self.state.handle(event)

            self.state.update()

            self.screen.fill((0x00, 0xb0, 0x00))

            self.state.draw(self.screen)

            pygame.display.flip()

def main():
    game = Game()
    game.main()

if __name__ == '__main__':
    main()
