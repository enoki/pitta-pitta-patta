#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from DefaultRules import *

class GameConfig:
    """ Game configuration information """

    def __init__(self):
        self.num_players = 2
        self.rules = RedBlackUpRules()
