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
        
    def collect_all(self,x,y):
        for c in self.cards:
            c.rect.x = x;
            c.rect.y = y;
            c.backSide();
            c.selected = 0
            c.parent = None
            c.child = None

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

    def get_card_at(self,idx):
        fc = self.cards.pop(idx)
        self.cards.append(fc)
        return fc  

    def __getitem__(self, index):
        return self.cards[index]
        
    def pop_cards(self, cards):
        for c in cards:
            self.cards.remove(c)
            self.cards.append(c)
    
    def get_cards(self,rect):
        r = None
        selCards = []
        for c in self.cards:
            if rect.contains(c.rect):
                c.selected = 1
                selCards.append(c)
                                
                # disconnect card
                if c.parent:
                    c.parent.child = None
                
                if c.child:
                    c.child.parent = None
                    self.drop_card(c.child)

                c.child = None
                c.parent = None

                # add to rectangle                    
                if not r:
                    r = pygame.Rect(c.rect)
                else:
                    r.union_ip(c.rect)
        if r:
            r.x-=3
            r.y-=3
            r.width+=6
            r.height+=6

            self.pop_cards(selCards)
                
            return(r,selCards)
        else:
            rect.size = (0,0)
            return(rect,[]) 
    
    def get_card(self,x,y,popsingle=0):
        for i in range(len(self.cards)-1,-1,-1):
            if self.cards[i].rect.collidepoint(x, y):
                fc = self.cards.pop(i)
                self.cards.append(fc)  
                if fc.parent:
                    fc.parent.child = None         
                    fc.parent = None
    
                if popsingle:
                    if fc.child:       
                        fc.child.parent = None
                        self.drop_card(fc.child)
                        fc.child = None
                else:                
                    c = fc.child
                    while c:
                        self.cards.remove(c)
                        self.cards.append(c)
                        c = c.child           
                return fc
                       
        return None

    def drop_card(self,card):
        idx = self.cards.index(card)
        for i in range(idx-1,-1,-1):
            if not self.cards[i].child and not self.cards[i].selected:
                if self.cards[i].rect.colliderect(card.rect):
                    self.cards[i].child = card
                    card.parent = self.cards[i]
                    return

    def drop_cards(self,cards):
        for c in cards:
            c.selected = 0
            c.child = None
            c.parent = None
            self.drop_card(c)

    def draw(self,surface):
        for c in self.cards:
            c.draw(surface)
