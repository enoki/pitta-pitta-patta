#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import pygame
import random
                             
class CardGroup:

    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def shuffle(self):
        rectbuf = []
        for c in self.cards:
            rectbuf.append(pygame.Rect(c.rect))

        random.shuffle(self.cards)        

        for i in range(len(rectbuf)):
            self.cards[i].rect = rectbuf[i]

    def reverse(self):
        self.cards.reverse()
        
    def collect_all(self,x,y):
        for c in self.cards:
            c.rect.x = x;
            c.rect.y = y;
            c.backSide();
            c.selected = 0

    def top_card(self):
        return self.cards[-1]

    def take_top_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def all_cards(self):
        for c in self.cards:
            yield c

    def empty(self):
        return len(self.cards) == 0

    def num_cards(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]
        
    def get_card(self,x,y):
        for card in self.cards:
            if card.rect.collidepoint(x, y):
                return card
                       
        return None

    def draw(self,surface):
        for c in self.cards:
            c.draw(surface)
