#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import louie
from Player import Player
from Computer import Computer
from FoundationPiles import FoundationPiles
from StatusBar import StatusBar

class PlayingField:
    """ The playing field comprises the foundation piles
        and each of the player piles. """

    game_over = louie.Signal()

    def __init__(self, game_config):
        self.players = []
        self.humans = []
        self.player = None
        self.rules = None
        self.foundation_piles = None
        self.status_bar = None
        self.game_config = game_config

        self.drawables = []
        self.handlers = []
        self.updateables = []

    def configure(self, match):
        """ Configures the playing field using the supplied GameConfig """
        self.match = match
        self.game = match.next_game()
        self.player = Player('You', 'blue', self.game_config)
        self.rules = self.game.rules
        self.foundation_piles = FoundationPiles(self.player,
                                                self.rules,
                                                self.game_config.num_players)
        self.status_bar = StatusBar(self.player, match)
        self.players = [self.player]
        self.humans = [self.player]

        for i in range(self.game_config.num_players-len(self.humans)):
            self.players.append(self.make_computer(i))

        assert(len(self.players) >= 2 and len(self.players) <= 4)

        louie.connect(self.on_game_over, Player.finished)

        self.drawables = [self.foundation_piles, self.status_bar]
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

    def get_round_count(self):
        return self.match.current_set().num_played_games()

    def record_scores(self):
        for player in self.players:
            self.game.add_score(player.get_name(), player.get_score())

    def game_score_summary(self):
        """ Returns a summary of all the player's score for the last game. """

        total_summary = []

        for player in self.players:
            summary = [player.get_name(),
                       player.num_good_cards(), 
                       -player.num_bad_cards() * 2,
                       player.get_score()]

            summary = map(str, summary)

            total_summary.append(summary)

        return total_summary

    def set_score_summary(self):
        """ Returns a summary of all the player's score for the current set. """
        total_summary = []

        set = self.match.current_set()

        for player in self.players:
            player_name = player.get_name()
            summary = [player_name]

            for game in set.all_played_games():
                summary.append(game.total_score_for(player_name))

            for game in set.all_unplayed_games():
                summary.append('-')

            summary.append(set.total_score_for(player_name))

            summary = map(str, summary)
            total_summary.append(summary)

        return total_summary

    def flip_cells(self, cell_index):
        for player in self.players:
            player.flip_cell(cell_index)
