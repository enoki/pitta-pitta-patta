#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import louie

if __name__ == '__main__':
    class Button:
        """ Mock for test below """
        clicked = louie.Signal()

        def __init__(self):
            self.checked = False

        def set_checked(self, checked=True):
            self.checked = checked

        def is_checked(self):
            return self.checked
else:
    from Button import Button


class ButtonGroup:
    """ A group of buttons which may be mutually exclusively checked.
        If desired, allows multiple buttons to be checked at once... """

    def __init__(self, buttons=None, exclusive=True):
        """ Set to mutually exclusive. """
        self.exclusive = exclusive
        if buttons:
            self.buttons = buttons
        else:
            self.buttons = []

        self.connect()

    def add_button(self, button):
        self.buttons.append(button)
        self.connect()

    def set_buttons(self, buttons):
        self.buttons = buttons
        self.connect()

    def connect(self):
        self.handlers = []

        for button in self.buttons:
            on_click = self.make_on_click(button)
            self.handlers.append(on_click)
            louie.connect(on_click, Button.clicked, button)

    def make_on_click(self, button):
        """ Creates a closure that checks the button. """
        def on_click():
            self.make_exclusive()
            button.set_checked(True)

        return on_click

    def make_exclusive(self):
        if self.exclusive:
            for button in self.buttons:
                button.set_checked(False)

    def set_check_color(self, color):
        for button in self.buttons:
            button.set_check_color(color)

def main():
    """ Simple Test """
    g = ButtonGroup()
    button1 = Button()
    button2 = Button()
    g.set_buttons([button1, button2])

    print "checking button1"
    louie.send(Button.clicked, button1)
    print "button1 checked? " + str(button1.is_checked())
    print "button2 checked? " + str(button2.is_checked())

    print "checking button2"
    louie.send(Button.clicked, button2)
    print "button1 checked? " + str(button1.is_checked())
    print "button2 checked? " + str(button2.is_checked())

if __name__ == '__main__':
    main()
