import pygame

class CardLocation:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.rect = pygame.Rect(x, y, width, height)

    def has(self, card):
        """ True if this location contains the card. """
        return card.rect.contains(self.rect)

    def contains(self, x, y):
        return self.rect.collidepoint(x, y)

    def grab_cards(self, cards):
        x = 0
        for card in cards:
            self.grab_card_(card, x)
            if x > -12:
                x -= 4

    def grab_card_(self, card, x):
        card.rect.x = self.rect.x + x
        card.rect.y = self.rect.y

    def grab_card(self, card):
        card.rect.x = self.rect.x
        card.rect.y = self.rect.y

    def position(self):
        return (self.rect.x, self.rect.y)
