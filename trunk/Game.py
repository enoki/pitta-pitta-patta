#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

class Game:
    """ A game is played with rules and has a name.
        The score is also kept for a game. """

    def __init__(self, rules, name):
        self.rules = rules
        self.name = name
        self.scores = {}

    def add_score(self, name, score):
        self.scores[name] = score
