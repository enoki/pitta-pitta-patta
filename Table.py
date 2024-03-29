#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from Color import Color

class RightSideBorder:
    """ A border to add to the right side of a cell. """
    def draw(self, surface, cell_rect, color):
        pygame.draw.line(surface, color,
                         cell_rect.topright, cell_rect.bottomright, 3)

class BottomSideBorder:
    """ A border to add to the bottom of a cell. """
    def draw(self, surface, cell_rect, color):
        pygame.draw.line(surface, color,
                         cell_rect.bottomleft, cell_rect.bottomright, 3)


class Cell:
    """ A cell in a table. """

    def __init__(self, text, font, text_color, background_color):
        self.text = text
        self.font = font
        self.text_color = text_color
        self.border_color = text_color
        self.background_color = background_color
        self.image = None
        self.borders = []
        self.rect = pygame.Rect(0,0,0,0)

    def render(self):
        self.image = self.font.render(self.text, 1, self.text_color)
        self.rect = self.image.get_rect()

    def get_rect(self):
        return self.rect

    def pos(self):
        return self.rect.topleft

    def width(self):
        return self.rect.width

    def height(self):
        return self.rect.height

    def draw(self, surface, x, y):
        if self.rect:
            self.rect.topleft = (x, y)
            surface.fill(self.background_color, self.rect)
            surface.blit(self.image, self.rect)

        for border in self.borders:
            border.draw(surface, self.rect, self.border_color)

    def set_text(self, text):
        self.text = text

    def set_font(self, font):
        self.font = font
        self.render()

    def set_text_color(self, text_color):
        self.text_color = text_color
        self.render()

    def set_background_color(self, background_color):
        self.background_color = background_color

    def set_width(self, width):
        self.rect.width = width

    def add_border(self, border):
        self.borders.append(border)

    def clear_borders(self):
        self.borders = []


class Table:
    """ A simple table widget for displaying on pygame surfaces. """

    def __init__(self, font, text_color, background_color, data=None, title=''):
        self.cells = []
        self.font = font
        self.text_color = text_color
        self.background_color = background_color
        self.titles = []
        self.x, self.y = (0, 0)
        self.row_height = 0
        self.spacing = ' '

        self.set_title(title)
        self.set_data(data)

    def set_data(self, data):
        if data:
            self.make_cells(data)
            self.render()

    def set_title(self, title):
        if len(title) > 0:
            title_text = title.split('\n')

            self.titles = []

            for line in title_text:
                cell = Cell(line, self.font, self.text_color, self.background_color)
                cell.add_border(BottomSideBorder())
                self.titles.append(cell)

    def cell_at(self, row, col):
        if self.empty():
            return None

        assert(row < self.num_rows() and col < self.num_cols())

        return self.cells[row][col]

    def make_cells(self, data):
        self.cells = []

        for row in data:
            self.cells.append([])

            for text in row:
                text_with_spacing = self.spacing + text + self.spacing
                cell = Cell(text_with_spacing,
                            self.font,
                            self.text_color,
                            self.background_color)
                self.cells[-1].append(cell)
            
    def render(self):
        for cell in self.each_cell():
            cell.render()

        for title in self.titles:
            title.render()

        self.calc_dimensions()
        
    def calc_dimensions(self):
        self.row_height = self.calc_row_height()
        col_widths = self.calc_col_widths()

        # set the column widths
        for row, col in self.each_index():
            cell = self.cell_at(row, col)
            cell.set_width(col_widths[col])

    def calc_row_height(self):
        row_height = 0
        for cell in self.each_cell():
            row_height = max(row_height, cell.height())
        return row_height

    def calc_col_widths(self):
        col_widths = {}

        for row, col in self.each_index():
            cell = self.cell_at(row, col)

            if col_widths.has_key(col):
                col_widths[col] = max(col_widths[col], cell.width())
            else:
                col_widths[col] = cell.width()

        return col_widths

    def draw(self, surface):
        self.x = (surface.get_width() - self.get_width()) / 2
        y = self.y

        for title in self.titles:
            x = (surface.get_width() - title.width()) / 2
            title.draw(surface, x, y)

        for row in self.cells:
            x = self.x
            y += self.row_height

            for cell in row:
                cell.draw(surface, x, y)

                x += cell.width()

    def set_right_col_border(self, col):
        for cell in self.each_col(col):
            cell.add_border(RightSideBorder())

    def set_bottom_row_border(self, row):
        for cell in self.each_row(row):
            cell.add_border(BottomSideBorder())

    def set_col_font(self, col, font):
        for cell in self.each_col(col):
            cell.set_font(font)

    def set_row_font(self, row, font):
        for cell in self.each_row(row):
            cell.set_font(font)

    def set_col_bg_color(self, col, color):
        for cell in self.each_col(col):
            cell.set_background_color(color)

    def set_row_bg_color(self, row, color):
        for cell in self.each_row(row):
            cell.set_background_color(color)

    def each_index(self):
        num_rows = self.num_rows()

        for row in range(0, num_rows):
            for col in range(0, len(self.cells[row])):
                yield row, col

    def each_cell(self):
        for row in self.cells:
            for cell in row:
                yield cell

    def each_col(self, col):
        for row in self.cells:
            if len(row) > col:
                yield row[col]

    def each_row(self, row):
        for cell in self.cells[row]:
            yield cell

    def empty(self):
        return self.num_rows() == 0 or self.num_cols == 0

    def num_rows(self):
        return len(self.cells)

    def num_cols(self):
        if self.num_rows() <= 0:
            return 0

        return len(self.cells[0])

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def set_x(self, x):
        self.x = x

    def get_height(self):
        return self.row_height * (self.num_rows() + 1 + len(self.titles))

    def get_width(self):
        if self.num_rows() == 0:
            return 0

        width = 0

        first_row = self.cells[0]
        for cell in first_row:
            width += cell.width()

        return width

    def get_size(self):
        return (self.get_width(), self.get_height())

    def handle(self, event):
        pass

