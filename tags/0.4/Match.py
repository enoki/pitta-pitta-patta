#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Set import Set

class Match:
    """ A match is an arbitrary sequence of sets. """

    def __init__(self):
        self.sets = []
        self.set = self.next_set()

    def next_game(self):
        if self.set.empty():
            self.set = self.next_set()

        game = self.set.next_game()
        return game

    def next_set(self):
        set = Set()
        self.sets.append(set)
        self.set = set
        return set

    def all_sets(self):
        for set in self.sets:
            yield set

    def current_set(self):
        return self.set

    def total_score_for(self, player_name):
        total = 0

        for set in self.all_sets():
            total += set.total_score_for(player_name)

        return total
