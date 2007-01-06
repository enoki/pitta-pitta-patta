#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from DefaultRules import *
from Game import Game

class Set:
    """ A set is a prefined collection of six games. """

    def __init__(self):
        rules_sequence = [RedBlackUpRules(),
                          SameColorUpRules(),
                          SameSuitUpRules(),
                          RedBlackDownRules(),
                          SameColorDownRules(),
                          SameSuitDownRules()]

        round_names = ['Red Black Up',
                       'Same Color Up',
                       'Same Suit Up',
                       'Red Black Down',
                       'Same Color Down',
                       'Same Suit Down']

        self.games = []

        for rules, name in zip(rules_sequence, round_names):
            self.games.append(Game(rules, name))

        self.played_games = []

    def next_game(self):
        game = self.games.pop(0)
        self.played_games.append(game)
        return game

    def current_game(self):
        return self.played_games[-1]

    def all_played_games(self):
        for game in self.played_games:
            yield game

    def all_unplayed_games(self):
        for game in self.games:
            yield game

    def num_played_games(self):
        return len(self.played_games)

    def num_unplayed_games(self):
        return len(self.games)

    def num_total_games(self):
        return self.num_played_games() + self.num_unplayed_games()

    def empty(self):
        return len(self.games) <= 0

    def total_score_for(self, player_name):
        total = 0

        for game in self.all_played_games():
            total += game.scores[player_name]

        return total
