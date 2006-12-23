#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from CardImages import CardImages
from CardGroup import CardGroup
from Card import Card

class SharedDeck:
    card_images = None

def Deck():
    """ Creates a deck of cards. """

    if not SharedDeck.card_images:
        SharedDeck.card_images = CardImages()

    ci = SharedDeck.card_images

    cards = []

    for number, suit, image in ci.images():
        cards.append(Card(number, suit, image, ci.get_back(), 30, 30))

    deck = CardGroup(cards)
    deck.shuffle()

    return deck
