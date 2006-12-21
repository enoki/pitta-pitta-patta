#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import louie
from EmptyCard import EmptyCard
from CardLocation import CardLocation


class CardCell:
    """ A single cell that holds a card. """

    grabbed_card = louie.Signal()

    def __init__(self):
        self.card = EmptyCard()
        self.location = CardLocation()

    def set_size(self, width, height):
        " Sets the size of this location "
        self.location.rect.width = width
        self.location.rect.height = height

    def move_to(self, x, y):
        " Moves this location "
        self.location.rect.x = x
        self.location.rect.y = y

    def take_from(self, deck):
        " Sets this card to the deck's top card "
        if not deck.empty():
            self.card = deck.take_top_card()

    def calibrate(self):
        " Prepare cards for display "
        self.location.grab_card(self.card)
        self.resize()

    def face_up(self):
        self.card.face_up()

    def face_down(self):
        self.card.face_down()

    def resize(self):
        " Resizes the location to the card in it "
        card_rect = self.card.rect
        self.set_size(card_rect.width, card_rect.height)

    def draw(self, surface):
        " Draws the card "
        self.card.draw(surface)

    def has(self, card):
        " True if the card is at this location "
        return location.has(card)

    def is_empty(self):
        " True if the card is empty "
        return str(self.card) == EmptyCard.id

    def set_card(self, card):
        " Sets the cell's card "
        self.card = card

    def get_card(self):
        " Returns the cell's card "
        return self.card

    def contains(self, card):
        " True if the card is contained in this cell "
        return self.card is card

    def contains_point(self, x, y):
        " True if the cell's card contains the point "
        return self.card.rect.collidepoint(x, y)

    def set_empty(self):
        " Makes the cell empty "
        self.card = EmptyCard()

    def position(self):
        " Returns the cell's topleft position "
        return self.location.rect.topleft

    def grab(self, card):
        " Grabs the card "
        (x, y) = self.position()
        card.move_to(x, y)
        self.set_card(card)
        louie.send(CardCell.grabbed_card, card=card)

