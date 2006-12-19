#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame

class PlayingCard:
    """ A simple view of a playing card. """

    (Ace, One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King) = range(14)
    (Clubs, Diamonds, Hearts, Spades) = range(4)
    (Red, Black) = range(2)

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

                             
class Card(PlayingCard):
    """ A playing card visible on the screen. """

    def __init__(self, index, frontImage, backImage, x=0, y=0):
        number = index / 4
        suit = index % 4
        PlayingCard.__init__(self, number, suit)
        self.bimg = backImage
        self.fimg = frontImage
        self.img = backImage
        self.side = 0
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.child = None
        self.parent = None
        self.selected = 0

    def flip(self):
        if self.side==1:
            self.side = 0
            self.img = self.bimg
        else:
            self.side = 1
            self.img = self.fimg

    def backSide(self):
        self.side = 0
        self.img = self.bimg

    def frontSide(self):
        self.side = 1
        self.img = self.fimg

    def setSide(self, side):
        if side:
            self.img = self.fimg
        else:
            self.img = self.bimg
        self.side = side
       
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        if self.child:
            self.child.move(dx,dy)

    def draw(self, surface):
        surface.blit(self.img,self.rect.topleft)
