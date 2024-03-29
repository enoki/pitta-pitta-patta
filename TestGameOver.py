#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Application import Application
from GameConfig import GameConfig

def main():
    """ Tests the game over state. """
    app = Application()
    config = app.game_config
    config.home_pile_size = 1
    app.goto_prepare()
    app.main()

if __name__ == '__main__':
    main()
