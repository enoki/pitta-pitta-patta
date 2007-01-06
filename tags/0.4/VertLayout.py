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
        if len(self.widgets) > 0:
            y = self.widgets[0].get_y()

        for widget in self.widgets:
            widget.set_y(y)
            y += widget.get_height()
