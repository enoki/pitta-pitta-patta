from CardImages import CardImages
from CardGroup import CardGroup
from Card import Card

class Deck:
    def __init__(self):
        ci = CardImages()

        cards = []

        for i in range(52):
            cards.append(Card(ci.get_card(i), ci.get_back(), 30, 30))

        self.card_group = CardGroup(cards)
        self.card_group.shuffle()

    def get_card(self, x, y):
        return self.card_group.get_card(x, y)

    def drop_card(self, card):
        return self.card_group.drop_card(card)

    def draw(self, surface):
        self.card_group.draw(surface)
