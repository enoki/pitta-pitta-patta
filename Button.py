#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import louie
from Color import Color
from Label import Label

class Button(Label):
    """ A generic button for displaying on pygame surfaces. """

    clicked = louie.Signal()

    def __init__(self, font, text_color, background_color, selected_color,
                 y, text):
        Label.__init__(self, font, text_color, background_color, y, text)
        self.normal_color = background_color
        self.selected_color = selected_color
        self.border_rect = pygame.Rect(0, 0, 0, 0)
        self.border_width = 3
        self.checked = False
        self.check_color = Color.black

    def set_text(self, text):
        Label.set_text(self, text)
        self.calculate_border()

    def calculate_border(self):
        self.border_rect = self.background_rect
        self.border_rect.width -= 5
        self.border_rect.height -= 1

    def draw(self, surface):
        Label.draw(self, surface)
        self.draw_check(surface)

    def draw_check(self, surface):
        if self.checked:
            x, y = self.position(surface)
            x -= 10
            pygame.draw.circle(surface, self.check_color, (x, y) , 3)

    def position(self, surface):
        """ Note: this returns the position of the first line only. """
        if len(self.images) > 0:
            centerx = surface.get_width() / 2
            image_rect = self.images[0].get_rect(centerx=centerx, y=self.y)
            return (image_rect.left, image_rect.centery)

        return (0, 0)

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

    def set_checked(self, checked=True, check_color=Color.black):
        self.checked = checked
        self.check_color = check_color

    def is_checked(self):
        return self.checked
