#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Card import Card

class EmptyCard(Card):
    """ A placeholder card. """

    def __init__(self):
        pass

    def flip(self):
        pass

    def face_down(self):
        pass

    def face_up(self):
        pass

    def move(self, dx, dy):
        pass

    def move_to(self, x, y):
        pass

    def draw(self, surface):
        pass

    def __str__(self):
        return 'empty'
