#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from SkillLevels import *
from Match import Match

class GameConfig:
    """ Game configuration information """

    def __init__(self):
        self.num_players = 4
        self.computer_skill = NormalSkillLevel()
        self.home_pile_size = 13
        self.match = Match()
