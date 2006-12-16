from Deck import Deck
from CardGroup import CardGroup

class Player:
    def __init__(self):
        self.deck = Deck()

        self.home_pile = CardGroup()
        self.cell_cards = CardGroup()

        for i in range(13):
            self.home_pile.add_card(self.deck.take_top_card())

        for i in range(3):
            self.cell_cards.add_card(self.deck.take_top_card())

        left_margin = 10 
        card_width = self.deck.top_card().rect.width

        self.deck.collect_all(left_margin + card_width * 2, 370)

        self.home_pile.collect_all(left_margin, 250)

        self.cell_cards.collect_all(left_margin, 250)

        x = card_width * 2
        for card in self.cell_cards.all_cards():
            card.rect.x += x
            x += card_width * 1.5

        self.home_pile.top_card().flip()

        self.drawables = [self.deck, self.home_pile, self.cell_cards]

    def draw(self, surface):
        for drawable in self.drawables:
            drawable.draw(surface)

    def handle(self, event):
        if event.type == pygame.MOUSEDOWN:
            pass
        # TODO
