import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("diamonds", 7)
        self.card2 = Card("clubs", 5)

        self.cards = [self.card1, self.card2]

    def test_if_card_is_an_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self.card1))

    def test_can_find_highest_card(self):
        self.assertEqual(self.card1, CardGame.highest_card(self.card1, self.card2))

    def test_can_calculate_card_total(self):
        self.assertEqual("You have a total of 12", CardGame.cards_total(self.cards))
