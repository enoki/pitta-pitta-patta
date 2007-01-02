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
        self.game_config = game_config
        self.game = self.game_config.match.next_game()
        self.player = Player('You', game_config)
        self.rules = self.game.rules
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
        return Computer(self.rules, self.foundation_piles, self.game_config,
                        position)

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
        self.record_scores()
        louie.send(PlayingField.game_over)

    def get_winner(self):
        high_score = 0 - self.player.home_pile.initial_size * 2
        winner = None

        for player in self.players:
            score = player.get_score()

            if score > high_score:
                high_score = score
                winner = player

        return winner

    def get_round_name(self):
        return self.game.name

    def record_scores(self):
        for player in self.players:
            self.game.add_score(player, player.get_score())
