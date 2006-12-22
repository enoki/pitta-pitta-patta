#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Label import Label

class Button(Label):
    """ A generic button for displaying on pygame surfaces. """

    clicked = louie.Signal()

    def __init__(self, font, text_color, background_color, border_color, y=0, text=None):
        Label.__init__(self, font, text_color, background_color, y, text)
        self.border_color = border_color
        self.border_rect = pygame.Rect(0, 0, 0, 0)
        self.border_width = 3

    def set_text(self, text):
        Label.set_text(self, text)
        self.calculate_border()

    def calculate_border(self):
        self.border_rect = self.background_rect
        self.border_rect.width -= 5
        self.border_rect.height -= 1

    def draw(self, surface):
        Label.draw(self, surface)
        self.draw_border(surface)

    def draw_border(self, surface):
        pygame.draw.rect(surface, self.border_color, self.border_rect,
                         self.border_width)

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos[0], event.pos[1]

                if self.background_rect.collidepoint(x, y):
                    louie.send(Button.clicked, self)

