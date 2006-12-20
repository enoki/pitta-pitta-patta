#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from CardImages import CardImages
from CardGroup import CardGroup
from Card import Card

def Deck():
    """ Creates a deck of cards. """

    ci = CardImages()

    cards = []

    for number, suit, image in ci.images():
        cards.append(Card(number, suit, image, ci.get_back(), 30, 30))

    deck = CardGroup(cards)
    deck.shuffle()

    return deck
