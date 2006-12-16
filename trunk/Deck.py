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

    for i in range(52):
        cards.append(Card(ci.get_card(i), ci.get_back(), 30, 30))

    deck = CardGroup(cards)
    deck.shuffle()

    return deck
