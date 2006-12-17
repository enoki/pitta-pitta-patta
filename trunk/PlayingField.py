#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Player import Player
from FoundationPiles import FoundationPiles

class Computer:
    """ The computer AI player. """

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
        self.foundation_piles = FoundationPiles(self.player)

        self.drawables = [self.player, self.computer, self.foundation_piles]
        self.handlers = [self.player, self.computer, self.foundation_piles]

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def handle(self, event):
        for handler in self.handlers:
            handler.handle(event)
