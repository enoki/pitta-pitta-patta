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

    (NorthWest, NorthEast, SouthEast) = range(3)

    def __init__(self, rules, foundation_piles, game_config, position):
        self.position = position
        name = self.get_position_name(position)
        Player.__init__(self, name, game_config)
        self.rules = rules
        self.foundation_piles = foundation_piles
        self.last_move_time = pygame.time.get_ticks()
        self.last_deal_time = pygame.time.get_ticks()
        self.time_to_deal = self.get_fast_time_to_deal()
        self.time_to_think = self.get_time_to_think()

    def handle(self, event):
        pass

    def set_locations(self):
        """ Position cards """
        if self.position == Computer.NorthWest:
            self.set_north_west()
        elif self.position == Computer.NorthEast:
            self.set_north_east()
        if self.position == Computer.SouthEast:
            self.set_south_east()

    def set_north_west(self):
        """ Puts the cards in the north-west position. """
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

    def set_north_east(self):
        """ Puts the cards in the north-east position. """
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

    def set_south_east(self):
        """ Puts the cards in the south-east position. """
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

    def get_position_name(self, position):
        if self.position == Computer.NorthWest:
            return 'Grant (North-West)'
        elif self.position == Computer.NorthEast:
            return 'Bob (North-East)'
        if self.position == Computer.SouthEast:
            return 'Susan (South-East)'

    def update(self):
        """ Handle a clock tick. """
        Player.update(self)

        if pygame.time.get_ticks() - self.last_deal_time > self.time_to_deal:
            self.last_deal_time = pygame.time.get_ticks()
            self.time_to_deal = self.get_fast_time_to_deal()
            self.deal_card()

            if self.xxxcount == 0:
                if random.random() < 0.9:
                    if self.make_best_move_using(self.discard_pile):
                        self.last_move_time = pygame.time.get_ticks()
                        return

        if pygame.time.get_ticks() - self.last_move_time > self.time_to_think:
            self.last_move_time = pygame.time.get_ticks()
            self.time_to_think = self.get_time_to_think()

            self.make_random_move()

    def get_time_to_think(self):
        # easy
        #self.time_to_think = 2000
        # medium
        #self.time_to_think = 1000
        # hard
        #self.time_to_think = 800
        return random.randint(2000, 3000)

    def get_fast_time_to_deal(self):
        return random.randint(500, 800)
        # This seems to work okay...
        #return random.randint(300, 600)

    def get_slow_time_to_deal(self):
        return random.randint(1000, 1300)

    def make_best_move(self):
        """ Move the first available card. """
        for clickable in self.clickables:
            if self.make_best_move_using(clickable):
                return

    def make_random_move(self):
        """ Consider making a move in each clickable category """
        for clickable in self.clickables:
            #if random.random() < 0.65:
            #if random.random() < 0.75:
            # This seems to work well also...
            if random.random() < 0.85:
            # This is hard...
            #if random.random() < 0.95:
                if self.make_best_move_using(clickable):
                    return

    def make_best_move_using(self, clickable):
        """ Move the first available card from the cards in clickable. """
        if clickable:
            cards = clickable.get_available_cards()
            for card in cards:
                piles = []
                empty_piles, nonempty_piles = \
                        self.get_empty_and_nonempty_in(self.foundation_piles.piles)

                # consider a random sample of at most four nonempty piles
                if len(nonempty_piles) >= 4:
                    piles = random.sample(nonempty_piles, 4)
                else:
                    piles = nonempty_piles

                # always consider an empty pile if one exists
                if len(empty_piles) > 0:
                    piles.append(empty_piles[0])

                for pile in piles:
                    if self.rules.is_valid(card, pile):
                        clickable.transfer(card, pile)
                        self.inc_score()
                        self.time_to_deal = self.get_slow_time_to_deal()
                        return True

        return False

    def get_empty_and_nonempty_in(self, piles):
        """ Returns the empty and nonempty piles in the provided list. 
            Returns a tuple (empty, nonempty) """
        empty = []
        non_empty = []

        for pile in piles:
            if pile.empty():
                empty.append(pile)
            else:
                non_empty.append(pile)

        return (empty, non_empty)

    def get_shuffled_foundation_piles(self):
        """ Returns a copy of the foundation piles in random order. """
        piles = copy.copy(self.foundation_piles.piles)
        random.shuffle(piles)
        return piles
