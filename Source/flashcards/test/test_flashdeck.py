import unittest
from flashcards.deck import Deck
from flashcards.card import Card

TEST_CARD_0 = Card("Card 0", "Description 0")
TEST_CARD_1 = Card("Card 1", "Description 1")
TEST_CARD_2 = Card("Card 2", "Description 2")
TEST_CARD_3 = Card("Card 3", "Description 3")

CARD_COUNT = 4

CARDS_SORTED = [TEST_CARD_0, TEST_CARD_1, TEST_CARD_2, TEST_CARD_3]
CARDS_UNSORTED = [TEST_CARD_1, TEST_CARD_3, TEST_CARD_0, TEST_CARD_2]

class Test (unittest.TestCase):
    
    def setUp(self):
        
        self._deck_empty     = Deck(None, 'Empty Deck')
        self._deck_sorted    = Deck(CARDS_SORTED, 'Sorted Deck')
        self._deck_unsorted  = Deck(CARDS_UNSORTED, 'Unsorted Deck')

    def test_card(self):
        
        result = self._deck_sorted.card(0)
        self.assertEquals(result, TEST_CARD_0)
    
    def test_copy(self):
        
        new_deck_sorted = self._deck_sorted.copy()
        self.assertEquals(new_deck_sorted.count, CARD_COUNT)
        self.assertEquals(new_deck_sorted.card(0), TEST_CARD_0)

    def test_count(self):

        result = self._deck_sorted.count
        self.assertEquals(result, CARD_COUNT)
    
    def test_count_deck_empty(self):
        
        result = self._deck_empty.count
        self.assertEquals(result, 0)
        
    def test_is_empty(self):
        
        self.assertFalse(self._deck_sorted.is_empty())
    
    def test_is_empty_deck_empty(self):
        
        self.assertTrue(self._deck_empty.is_empty())
    
    def test_is_not_empty(self):
        
        self.assertTrue(self._deck_sorted.is_not_empty())
    
    def test_sort(self):
        
        self._deck_unsorted.sort()
        
        for card_pair in zip (CARDS_SORTED, self._deck_unsorted.cards):
            self._test_cards_match(card_pair[0], card_pair[1])
    
    def _test_cards_match (self, expected_card, actual_card):
        
        expected_title = "Expected: " + expected_card.title if expected_card is not None else "[None]"
        actual_title = "actual: " + actual_card.title if actual_card is not None else "[None]"

        self.assertEquals(expected_card, actual_card, expected_title + ". " + actual_title)
        