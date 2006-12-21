#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import random
import copy
from Player import Player

class Computer(Player):
    """ The computer AI player. """

    (North, West, East) = range(3)

    def __init__(self, rules, foundation_piles, position):
        self.position = position
        Player.__init__(self)
        self.rules = rules
        self.foundation_piles = foundation_piles
        self.last_move_time = pygame.time.get_ticks()
        self.last_deal_time = pygame.time.get_ticks()
        self.time_to_deal = random.randint(600, 900)
        # easy
        #self.time_to_think = 1000
        # medium
        #self.time_to_think = 800
        # hard
        #self.time_to_think = 600
        self.time_to_think = random.randint(1000, 2000)

    def handle(self, event):
        pass

    def set_locations(self):
        """ Position cards """
        if self.position == Computer.North:
            self.set_north()
        elif self.position == Computer.West:
            self.set_west()
        if self.position == Computer.East:
            self.set_east()

    def set_north(self):
        """ Puts the cards in the north position. """
        some_card = self.home_pile.top_card()
        card_width, card_height = some_card.rect.width, some_card.rect.height
        left_margin, hand_top_margin = 10, 0
        top_margin = hand_top_margin + card_height + 10

        x = left_margin
        y = top_margin

        # "Top" row
        self.home_pile.move_to(x, y)
        x += card_width * 1.7 
        distance_between = card_width * 1.3
        self.cell_cards.move_to(x, y, distance_between)

        x = left_margin + card_width * 0.2
        y = hand_top_margin

        # "Bottom" row
        self.stock_pile.move_to(x, y)
        x += card_width * 1.5
        self.discard_pile.move_to(x, y)
        x += card_width * 1.5
        self.right_hand.move_to(x, y, 40)

    def set_west(self):
        """ Puts the cards in the west position. """
        some_card = self.home_pile.top_card()
        card_width, card_height = some_card.rect.width, some_card.rect.height
        left_margin, hand_top_margin = 450, 0
        top_margin = hand_top_margin + card_height + 10

        x = left_margin
        y = top_margin

        # "Top" row
        self.home_pile.move_to(x, y)
        x += card_width * 1.5
        distance_between = card_width * 1.3
        self.cell_cards.move_to(x, y, distance_between)

        x = left_margin + card_width * 0.2
        y = hand_top_margin

        # "Bottom" row
        self.stock_pile.move_to(x, y)
        x += card_width * 1.5
        self.discard_pile.move_to(x, y)
        x += card_width * 1.5
        self.right_hand.move_to(x, y, 40)

    def set_east(self):
        """ Puts the cards in the east position. """
        some_card = self.home_pile.top_card()
        card_width, card_height = some_card.rect.width, some_card.rect.height
        left_margin, top_margin = 450, 450
        hand_top_margin = top_margin + card_height + 10

        x, y = left_margin, top_margin

        # Top row
        self.home_pile.move_to(x, y)
        x += card_width * 1.7 
        distance_between = card_width * 1.3
        self.cell_cards.move_to(x, y, distance_between)

        x = left_margin + card_width * 0.2
        y = hand_top_margin

        # Bottom row
        self.stock_pile.move_to(x, y)
        x += card_width * 1.5
        self.discard_pile.move_to(x, y)
        x += card_width * 1.5
        self.right_hand.move_to(x, y, 40)

    def update(self):
        """ Handle a clock tick. """
        Player.update(self)

        if pygame.time.get_ticks() - self.last_deal_time > self.time_to_deal:
            self.last_deal_time = pygame.time.get_ticks()
            self.deal_card()

            if self.xxxcount == 0:
                self.make_best_move_using(self.discard_pile)

        if pygame.time.get_ticks() - self.last_move_time > self.time_to_think:
            self.last_move_time = pygame.time.get_ticks()
            self.time_to_think = random.randint(1000, 2000)

            self.make_random_move()

    def make_best_move(self):
        """ Move the first available card. """
        for clickable in self.clickables:
            if self.make_best_move_using(clickable):
                return

    def make_random_move(self):
        """ Consider making a move in each clickable category """
        for clickable in self.clickables:
            if random.random() > 0.5:
                self.make_best_move_using(clickable)

    def make_best_move_using(self, clickable):
        """ Move the first available card from the cards in clickable. """
        if clickable:
            cards = clickable.get_available_cards()
            for card in cards:
                # consider the piles in random order
                piles = copy.copy(self.foundation_piles.piles)
                random.shuffle(piles)

                for pile in piles:
                    if self.rules.is_valid(card, pile):
                        clickable.transfer(card, pile)
                        return True

        return False
