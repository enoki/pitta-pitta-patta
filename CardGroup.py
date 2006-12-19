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
        """ Shuffles the cards in the group. """
        random.shuffle(self.cards)        

    def reverse(self):
        """ Reverses the order of cards in the group. """
        self.cards.reverse()

    def top_card(self):
        """ Returns the top card. """
        return self.cards[-1]

    def take_top_card(self):
        """ Returns the top card and removes it from this group. """
        return self.cards.pop()

    def add_card(self, card):
        """ Adds a card to the top of the group. """
        self.cards.append(card)

    def all_cards(self):
        """ Allow iteration over all of the cards. """
        for c in self.cards:
            yield c

    def empty(self):
        """ True if there are no cards in this group. """
        return len(self.cards) == 0

    def num_cards(self):
        """ Returns the number of cards in the group. """
        return len(self.cards)

    def __getitem__(self, index):
        """ Returns the card at the specified index. """
        return self.cards[index]

    def __setitem__(self, index, card):
        """ Puts a card at the specified index. """
        self.cards[index] = card

    def index(self, card):
        return self.cards.index(card)
        
    def get_card(self,x,y):
        """ Returns the card at the specified coordinates.
            If no card is available, returns None. """
        for card in self.cards:
            if card.rect.collidepoint(x, y):
                return card
                       
        return None

    def draw(self,surface):
        """ Draws each of the cards in the group. """
        for c in self.cards:
            c.draw(surface)
