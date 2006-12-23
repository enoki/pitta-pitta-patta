#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame

class Label:
    """ A generic label for displaying on pygame surfaces. """

    def __init__(self, font, text_color, background_color, y=0, text=None):
        self.images = []
        self.width, self.height = 0, 0
        self.text_color = text_color
        self.background_color = background_color
        self.font = font
        self.background_rect = None
        self.y = y
        self.horiz_margins = 20

        if text is not None:
            self.set_text(text)

    def set_text(self, text):
        """ Pass in a string to have this label display them. """
        self.create_text(text)
        self.calculate_size()
        self.create_background()

    def create_text(self, text):
        self.images = []
        self.width, self.height = 0, 0

        text_list = text.split('\n')

        for text_line in text_list:
            self.images.append(self.make_text_image(text_line))

    def make_text_image(self, text_line):
        return self.font.render(text_line, 1, self.text_color)

    def create_background(self):
        self.background_rect = pygame.Rect(0,0,0,0)
        self.background_rect.size = self.width, self.height

    def calculate_size(self):
        self.y_spacing = 0

        for image in self.images:
            rect = image.get_rect()
            self.width = max(self.width, rect.width)
            self.y_spacing = max(self.y_spacing, rect.height * 1.5)
            self.height += self.y_spacing

        self.width += self.horiz_margins

    def get_size(self):
        return (self.width, self.height)

    def get_height(self):
        return self.height

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def center_vertically_on(self, surface):
        self.set_y((surface.get_height() - self.get_height()) / 2)

    def draw(self, surface):
        self.center_x = surface.get_width() / 2

        self.draw_background(surface)

        y = self.y

        for image in self.images:
            image_rect = image.get_rect(centerx=self.center_x, y=y)
            surface.blit(image, image_rect)
            y += self.y_spacing

    def draw_background(self, surface):
        if self.background_rect:
            self.background_rect.centerx = self.center_x
            self.background_rect.y = self.y
            pygame.draw.rect(surface, self.background_color, self.background_rect)

    def empty(self):
        return len(self.images) == 0

    def handle(self, event):
        pass
