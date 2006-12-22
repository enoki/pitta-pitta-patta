#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from VertLayout import VertLayout

class RectContainer:
    """ A rectangular container for displaying on pygame surfaces.
        Just displays all its children with a rectangular background. """

    def __init__(self, background_color, widgets=None):
        self.widgets = []
        self.background_color = background_color
        self.background_rect = pygame.Rect(0, 0, 0, 0)

        if widgets is not None:
            self.create_ui(widgets)

    def create_ui(self, widgets):
        self.widgets = widgets
        self.set_layout()
        self.calculate_size()
        self.create_background()

    def set_layout(self):
        layout = VertLayout()
        for widget in self.widgets:
            layout.add(widget)
        layout.layout()

    def calculate_size(self):
        self.width, self.height = 0, 0
        for widget in self.widgets:
            width, height = widget.get_size()

            self.width = max(self.width, width)
            self.height += height

    def create_background(self):
        self.background_rect = pygame.Rect(0, 0, self.width, self.height)
        self.background_rect.y = self.get_y()

    def draw(self, surface):
        self.draw_background(surface)

        for widget in self.widgets:
            widget.draw(surface)

    def draw_background(self, surface):
        self.background_rect.centerx = surface.get_width() / 2
        pygame.draw.rect(surface, self.background_color, self.background_rect)

    def handle(self, event):
        for widget in self.widgets:
            widget.handle(event)
        
    def get_size(self):
        return width, height

    def get_height(self):
        return self.height

    def get_y(self):
        y = 0
        if len(self.widgets) > 0:
            widget = self.widgets[0]
            y = widget.get_y()
        return y

    def set_y(self, y):
        if len(self.widgets) > 0:
            widget = self.widgets[0]
            widget.set_y(y)
            self.set_layout()
