#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

class VertLayout:
    def __init__(self):
        self.widgets = []

    def add(self, widget):
        self.widgets.append(widget)

    def layout(self):
        y = 0
        for widget in self.widgets:
            y += widget.get_y()
            widget.set_y(y)
            y += widget.get_height()
