import unittest
from flashcards.deckmodeldefault import DeckModelDefault
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

        self._model_empty    = DeckModelDefault (self._deck_empty)
        self._model_sorted   = DeckModelDefault (self._deck_sorted)
        self._model_unsorted = DeckModelDefault (self._deck_unsorted)
    
    def test_card(self):
        
        result = self._model_sorted.card(0)
        self.assertEquals(result, TEST_CARD_0)
    
    def test_copy(self):
        
        new_model_sorted = self._model_sorted.copy()
        self.assertEquals(new_model_sorted.count, CARD_COUNT)
        self.assertEquals(new_model_sorted.card(0), TEST_CARD_0)

    def test_count(self):

        result = self._model_sorted.count
        self.assertEquals(result, CARD_COUNT)
    
    def test_count_model_empty(self):
        
        result = self._model_empty.count
        self.assertEquals(result, 0)
        
    def test_has_next(self):
        
        self.assertTrue(self._model_sorted._has_next())
        
        for i in range (CARD_COUNT):
            self._model_sorted.next_card()
            
        self.assertFalse(self._model_sorted._has_next())
        
    def test_has_next_model_empty(self):
        
        self.assertFalse(self._model_empty._has_next())
        
    def test_next_card(self):
        
        self._test_cards_match(TEST_CARD_0, self._model_sorted.current_card)
        self._test_cards_match(TEST_CARD_1, self._model_sorted.next_card())
        self._test_cards_match(TEST_CARD_2, self._model_sorted.next_card())
        self._test_cards_match(TEST_CARD_3, self._model_sorted.next_card())
        self.assertIsNone(self._model_sorted.next_card())
    
    def test_next_card_model_empty(self):
        
        self.assertIsNone(self._model_empty.next_card())
        
    def test_remove_card(self):
        
        # Remove 1st card. Test 1st card is now second card.

        self._model_sorted.remove_current_card()
        
        result = self._model_sorted.card(0)
        self._test_cards_match(TEST_CARD_1, result)
        
    def test_sort(self):
        
        self._model_unsorted.sort()
        
        for card_pair in zip (CARDS_SORTED, self._model_unsorted.cards):
            self._test_cards_match(card_pair[0], card_pair[1])
    
    def test_remove_card_model_empty(self):
        
        self._model_empty.remove_current_card()
        self.assertTrue(True, "Got here with no exceptions - Great!")

    def _test_cards_match (self, expected_card, actual_card):
        
        expected_title = "Expected: " + expected_card.title if expected_card is not None else "[None]"
        actual_title = "actual: " + actual_card.title if actual_card is not None else "[None]"

        self.assertEquals(expected_card, actual_card, expected_title + ". " + actual_title)
        