#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Player import Player

class Computer:
    """ The computer AI player. """

    def __init__(self):
        pass

    def draw(self, surface):
        pass

    def handle(self, event):
        pass

class FoundationPiles:
    """ The piles on which players drop stacks of ordered cards. """

    def __init__(self):
        pass

    def draw(self, surface):
        pass

    def handle(self, event):
        pass

class PlayingField:
    """ The playing field comprises the foundation piles
        and each of the player piles. """

    def __init__(self):
        self.player = Player()
        self.computer = Computer()
        self.foundation_piles = FoundationPiles()

        self.drawables = [self.player, self.computer, self.foundation_piles]
        self.handlers = [self.player, self.computer, self.foundation_piles]

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def handle(self, event):
        for handler in self.handlers:
            handler.handle(event)
