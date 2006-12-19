#!/usr/bin/env python
#
# Pitta-pitta-patta
# Released under the GPL version 2.0 or later.
#

import unittest
from DefaultRules import *
from UpRule import UpRule
from Card import PlayingCard
from Card import Card
from Pile import Pile

class TestUpRule(unittest.TestCase):
    def setUp(self):
        self.rule = UpRule()

    def test_starter(self):
        card = PlayingCard(PlayingCard.Ace, PlayingCard.Spades)
        self.assert_(self.rule.is_starter(card))

    def test_not_starter(self):
        card = PlayingCard(PlayingCard.Three, PlayingCard.Hearts)
        self.assert_(not self.rule.is_starter(card))

class TestRedBlackRule(unittest.TestCase):
    def setUp(self):
        self.rule = RedBlackRule()

    def test_starter(self):
        card = PlayingCard(PlayingCard.Ace, PlayingCard.Spades)
        self.assert_(self.rule.is_starter(card))

class TestRedBlackUpRules(unittest.TestCase):
    def setUp(self):
        self.rules = RedBlackUpRules()

    def test_starter(self):
        card = PlayingCard(PlayingCard.Ace, PlayingCard.Spades)
        self.assert_(self.rules.is_starter(card))

    def test_valid_with_empty_pile(self):
        card = PlayingCard(PlayingCard.Ace, PlayingCard.Spades)
        pile = Pile()
        self.assert_(self.rules.is_valid(card, pile))

if __name__ == '__main__':
    unittest.main()
