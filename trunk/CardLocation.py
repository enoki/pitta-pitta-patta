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
        for card in cards:
            self.grab_card(card)

    def grab_card(self, card):
        card.rect.x = self.rect.x
        card.rect.y = self.rect.y
