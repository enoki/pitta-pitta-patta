#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from Color import Color
from Label import Label

class StatusBar:
    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.rect = pygame.Rect(0,0,0,40)
        self.font = pygame.font.SysFont("Arial", 20)
        self.left_label = self.make_label(self.game.name)
        self.drawables = [self.left_label]

    def create_ui(self):
        pass

    def make_label(self, text):
        label = Label(self.font, Color.white, Color.medium_blue)
        label.set_text(text)
        return label

    def draw(self, surface):
        self.draw_background(surface)

        self.left_label.set_y(surface.get_height() - self.rect.height)

        for drawable in self.drawables:
            drawable.draw(surface)

    def draw_background(self, surface):
        self.rect.y = surface.get_height() - self.rect.height
        self.rect.width = surface.get_width()

        surface.fill(Color.medium_blue, self.rect)
