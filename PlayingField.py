#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import louie
from Player import Player
from Computer import Computer
from FoundationPiles import FoundationPiles
from DefaultRules import *

class PlayingField:
    """ The playing field comprises the foundation piles
        and each of the player piles. """

    game_over = louie.Signal()

    def __init__(self, num_players):
        self.player = Player('You')
        self.rules = RedBlackUpRules()
        self.foundation_piles = FoundationPiles(self.player, self.rules)
        self.computer = Computer(self.rules, self.foundation_piles, Computer.NorthWest)
        self.players = [self.player, self.computer]
        self.num_players = 4
        if self.num_players > 2:
            self.computer2 = Computer(self.rules, self.foundation_piles, Computer.SouthEast)
            self.players.append(self.computer2)
        if self.num_players > 3:
            self.computer3 = Computer(self.rules, self.foundation_piles, Computer.NorthEast)
            self.players.append(self.computer3)

        louie.connect(self.on_game_over, Player.finished)

        self.drawables = [self.foundation_piles]
        self.drawables.extend(self.players)
        self.handlers = [self.player, self.computer, self.foundation_piles]
        self.updateables = [self.foundation_piles]
        self.updateables.extend(self.players)

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def handle(self, event):
        for handler in self.handlers:
            handler.handle(event)

    def update(self):
        for updateable in self.updateables:
            updateable.update()

    def on_game_over(self):
        louie.send(PlayingField.game_over)
