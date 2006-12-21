#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

class PlayingCard:
    """ A simple view of a playing card. """

    (Zero, Ace, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten,
     Jack, Queen, King) = range(15)
    (Clubs, Diamonds, Hearts, Spades) = range(4)
    (Red, Black) = range(2)

    numbers = ['0', 'a', '2', '3', '4', '5', '6', '7', '8', '9', '10',
               'j', 'q', 'k']
    suits = ['c', 'd', 'h', 's']

    def __init__(self, number, suit):
        self._number = number
        self._suit = suit

        if self.suit() == Card.Clubs or self.suit() == Card.Spades:
            self._color = Card.Black
        else:
            self._color = Card.Red

    def number(self):
        return self._number

    def suit(self):
        return self._suit

    def color(self):
        return self._color

    def __str__(self):
        return PlayingCard.numbers[self.number()] + \
               PlayingCard.suits[self.suit()]
                             
class Card(PlayingCard):
    """ A playing card visible on the screen. """

    (front, back) = range(2)

    def __init__(self, number, suit, frontImage, backImage, x=0, y=0):
        PlayingCard.__init__(self, number, suit)
        self.bimg = backImage
        self.fimg = frontImage
        self.img = backImage
        self.side = Card.back
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.selected = 0
        self.destination = None
        (self.inc_x, self.inc_y) = (0, 0)

    def flip(self):
        if self.side == Card.front:
            self.side = Card.back
            self.img = self.bimg
        else:
            self.side = Card.front 
            self.img = self.fimg

    def face_down(self):
        self.side = Card.back 
        self.img = self.bimg

    def face_up(self):
        self.side = Card.front
        self.img = self.fimg

    def move(self, dx, dy):
        """ Moves the card relative to its current location. """
        self.rect.x += dx
        self.rect.y += dy

    def move_to(self, x, y):
        """ Moves the card to an absolute coordinate. """
        self.rect.x = x
        self.rect.y = y

    def position(self):
        return (self.rect.x, self.rect.y)

    def throw_to(self, destination):
        """ Throws the card to the destination.
            The destination must implement
                def take(card): return None
                def position(): return (x, y)
        """
        self.destination = destination
        destination_x, destination_y = destination.position()
        x, y = self.position()
        delta_x = destination_x - x
        delta_y = destination_y - y
        num_steps = 10
        self.inc_x = delta_x / num_steps
        self.inc_y = delta_y / num_steps

    def update(self):
        """ Called every frame to update the card. """
        if self.destination:
            if self.close_to(self.destination.position()):
                self.destination.grab(self)
                self.destination = None
            else:
                self.move(self.inc_x, self.inc_y)

    def draw(self, surface):
        surface.blit(self.img, self.rect.topleft)
