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
    new_game = louie.Signal()

    def __init__(self, playing_field):
        self.playing_field = playing_field
        self.text_images = []
        self.font = pygame.font.Font(None, 36)
        self.width = 0
        self.height = 0
        self.y_spacing = 0
        self.informative = False

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.toggle_informative()
            elif event.key == pygame.K_RETURN:
                self.new_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.new_game()
            elif event.button == 3:
                self.toggle_informative()

    def update(self):
        if len(self.text_images) > 0:
            return

        self.create_text()

    def create_text(self):
        self.text_images = []
        self.width, self.height = 0, 0

        self.text_images.append(self.make_text('Game over.'))
        self.text_images.append(self.make_text('  '))
        high_score = -26    # -(num_home_cards * 2)
        winning_player = None

        self.score_table_text = []

        for player in self.playing_field.players:
            score = player.get_score()
            text = player.get_name() + ': '
            text += str(score)
            if self.informative:
                text += '      ('
                text += str(score)
                text += ' = '
                text += str(player.num_good_cards())
                text += ' - '
                text += str(player.num_bad_cards())
                text += 'x2)'
            image = self.make_text(text)
            self.score_table_text.append(image)

            if score > high_score:
                high_score = score
                winning_player = player

        win_text = ""
        if winning_player == self.playing_field.player:
            win_text = 'You Win!'
        else:
            win_text = winning_player.get_name() + ' Wins!'
        self.text_images.append(self.make_text(win_text))
        self.text_images.append(self.make_text('  '))

        self.text_images.extend(self.score_table_text)

        self.text_images.append(self.make_text('  '))
        self.text_images.append(self.make_text('Press enter to start a new game'))
        if self.informative:
            self.text_images.append(self.make_text('Press space for less information'))
        else:
            self.text_images.append(self.make_text('Press space for more information'))

        for image in self.text_images:
            rect = image.get_rect()
            self.width = max(rect.width, self.width)
            self.y_spacing = rect.height * 1.5
            self.height += self.y_spacing

    def make_text(self, text):
        # Black
        #return self.font.render(text, 1, (10, 10, 10))
        # White
        return self.font.render(text, 1, (0xff, 0xff, 0xff))

    def draw(self, surface):
        self.playing_field.draw(surface)

        y = 0

        # Draw background behind the text
        center_x = surface.get_width() / 2
        background_rect = pygame.Rect(0,0,0,0)
        background_rect.size = (self.width + 20, self.height)
        background_rect.centerx=center_x
        pygame.draw.rect(surface, (0x00, 0x00, 0xb0), background_rect)

        # Draw the text line by line
        for image in self.text_images:
            text_pos = image.get_rect(centerx=center_x)
            text_pos.y = y
            surface.blit(image, text_pos)

            y += self.y_spacing

    def new_game(self):
        louie.send(GameOverState.new_game)

    def toggle_informative(self):
        self.informative = not self.informative
        self.create_text()
    

class Game:
    def __init__(self):
        pygame.init()

        self.num_players = 4

        if self.num_players == 2:
            self.screen = pygame.display.set_mode((430, 660))
        elif self.num_players > 2:
            self.screen = pygame.display.set_mode((850, 660))

        pygame.display.set_caption('Pitta Pitta Patta')

        self.create_states()

    def create_states(self):
        playing_field = PlayingField(self.num_players)
        louie.connect(self.end_game, PlayingField.game_over)

        start_state = StartState()
        playing_state = PlayingState(playing_field)
        game_over_state = GameOverState(playing_field)

        louie.connect(self.start_playing, StartState.finished)
        louie.connect(self.restart, GameOverState.new_game)

        self.states = { 'Start' : start_state,
                        'Playing' : playing_state,
                        'GameOver' : game_over_state }

        self.state = self.states['Playing']

    def end_game(self):
        self.state = self.states['GameOver']

    def start_playing(self):
        self.state = self.states['Playing']

    def restart(self):
        self.create_states()

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
