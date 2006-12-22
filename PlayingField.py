#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import louie
from Player import Player
from Computer import Computer
from FoundationPiles import FoundationPiles

class PlayingField:
    """ The playing field comprises the foundation piles
        and each of the player piles. """

    game_over = louie.Signal()

    def __init__(self):
        self.players = []
        self.humans = []
        self.player = None
        self.rules = None
        self.foundation_piles = None

        self.drawables = []
        self.handlers = []
        self.updateables = []

    def configure(self, game_config):
        """ Configures the playing field using the supplied GameConfig """
        self.player = Player('You')
        self.rules = game_config.rules
        self.foundation_piles = FoundationPiles(self.player,
                                                self.rules,
                                                game_config.num_players)
        self.players = [self.player]
        self.humans = [self.player]

        for i in range(game_config.num_players-len(self.humans)):
            self.players.append(self.make_computer(i))

        assert(len(self.players) >= 2 and len(self.players) <= 4)

        louie.connect(self.on_game_over, Player.finished)

        self.drawables = [self.foundation_piles]
        self.drawables.extend(self.players)
        self.handlers = [self.player, self.foundation_piles]
        self.updateables = [self.foundation_piles]
        self.updateables.extend(self.players)

    def make_computer(self, position):
        return Computer(self.rules, self.foundation_piles, position)

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
