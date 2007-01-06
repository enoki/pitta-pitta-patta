#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

from CardImages import CardImages
from CardGroup import CardGroup
from Card import Card

class SharedImages:
    """ Private class to store shared images. """
    card_images = None

def Deck(name):
    """ Creates a deck of cards. """

    if SharedImages.card_images is None:
        SharedImages.card_images = CardImages()

    ci = SharedImages.card_images

    cards = []

    back_image = ci.get_back(name)

    for number, suit, image in ci.images():
        cards.append(Card(number, suit, image, back_image, 30, 30))

    deck = CardGroup(cards)
    deck.shuffle()

    return deck
