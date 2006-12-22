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

    def __init__(self, font, text_color, background_color, selected_color, y=0, text=None):
        Label.__init__(self, font, text_color, background_color, y, text)
        self.normal_color = background_color
        self.selected_color = selected_color
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

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos[0], event.pos[1]

                if self.background_rect.collidepoint(x, y):
                    louie.send(Button.clicked, self)
                    
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos[0], event.pos[1]

            if self.background_rect.collidepoint(x, y):
                self.select()
            else:
                self.unselect()

    def select(self):
        self.background_color = self.selected_color

    def unselect(self):
        self.background_color = self.normal_color

