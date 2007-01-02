#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from Application import Application
from GameConfig import GameConfig

def main():
    app = Application()
    config = GameConfig()
    config.home_pile_size = 1
    app.goto_prepare(config)
    app.main()

if __name__ == '__main__':
    main()
