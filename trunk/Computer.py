#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
from Player import Player

class Computer(Player):
    """ The computer AI player. """

    def __init__(self, rules, foundation_piles):
        Player.__init__(self)
        self.rules = rules
        self.foundation_piles = foundation_piles
        self.last_time = pygame.time.get_ticks()

    def handle(self, event):
        pass

    def set_locations(self):
        """ Position cards """
        some_card = self.home_pile.top_card()
        card_width, card_height = some_card.rect.width, some_card.rect.height
        left_margin, hand_top_margin = 10, 0
        top_margin = hand_top_margin + card_height + 30

        x = left_margin
        y = top_margin

        # "Top" row
        self.home_pile.move_to(x, y)
        x += card_width * 2
        self.cell_cards.move_to(x, y, card_width * 1.5)

        y = hand_top_margin

        # "Bottom" row
        self.stock_pile.move_to(x, y)
        x += card_width * 1.5
        self.discard_pile.move_to(x, y)
        x += card_width * 1.5
        self.right_hand.move_to(x, y, 40)

    def update(self):
        """ Handle a clock tick. """
        Player.update(self)

        if pygame.time.get_ticks() - self.last_time > 700:
            self.last_time = pygame.time.get_ticks()

            self.deal_card()

            if self.xxxcount == 0:
                # Transfer the first available card
                for clickable in self.clickables:
                    if clickable:
                        cards = clickable.get_available_cards()
                        for card in cards:
                            for pile in self.foundation_piles.piles:
                                if self.rules.is_valid(card, pile):
                                    clickable.transfer(card, pile)
                                    return
