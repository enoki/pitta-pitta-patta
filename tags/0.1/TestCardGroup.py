#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import unittest
from CardGroup import CardGroup
from Card import PlayingCard

class TestCardGroup(unittest.TestCase):
    def setUp(self):
        self.cards = CardGroup()
        #
        self.bottom_card = PlayingCard(PlayingCard.Ace, PlayingCard.Spades)
        self.top_card = PlayingCard(PlayingCard.King, PlayingCard.Diamonds)
        #
        self.cards.add_card(bottom_card)
        self.cards.add_card(top_card)

    def test_top_card(self):
        self.assertEqual(self.top_card, self.cards.top_card())

    def test_take_top_card(self):
        self.assertEqual(self.top_card, self.cards.take_top_card())

if __name__ == '__main__':
    unittest.main()
