#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import logging
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
        card_rect = self.home_pile.top_card().rect
        card_width, card_height = card_rect.width, card_rect.height
        left_margin = 10
        hand_top_margin = 0
        top_margin = hand_top_margin + card_rect.height + 30

        self.home_pile.move_to(left_margin, top_margin)
        self.stock_pile.move_to(left_margin + card_width * 2, hand_top_margin)
        self.discard_pile.move_to(left_margin + card_width * 2  + card_width * 1.5, hand_top_margin)
        self.cell_cards.move_to(left_margin + card_width * 2, top_margin, card_width * 1.5)
        self.right_hand.move_to(left_margin + card_width * 2 + card_width * 1.5 * 2, hand_top_margin, 40)

    def update(self):
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
                                    pile.calibrate()
                                    return
