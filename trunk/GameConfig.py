#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from DefaultRules import *
from SkillLevels import *

class GameConfig:
    """ Game configuration information """

    def __init__(self):
        self.num_players = 2
        self.rules = RedBlackUpRules()
        self.round_name = 'Red Black Up'
        self.home_pile_size = 13
        self.computer_skill = NormalSkillLevel()
