#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

class State:
    def entered(self):
        pass

    def exited(self):
        pass

    def delay(self):
        pass

    def handle(self, event):
        pass

    def update(self):
        pass

    def clear_surface(self, surface):
        pass

    def draw(self, surface):
        pass
