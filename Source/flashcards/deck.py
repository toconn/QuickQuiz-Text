import operator
from random import shuffle
from ua.core.utils import listutils

class Deck:
    
    def __init__(self, cards, deck_name = None, source_path = None):
        
        self.deck_name = deck_name
        self.enabled = True
        self.source_path = source_path
        
        if cards is not None:
            self._cards = list(cards)
        else:
            self._cards = []

    @property
    def count(self):
        return listutils.count(self._cards)
    
    @property
    def cards(self):
        return self._cards
    
    @property
    def sorted_cards(self):    
        sorted_cards = list(self._cards)
        sorted_cards.sort(key=operator.attrgetter('title'))
    
        return sorted_cards
    
    def add_cards(self, card_list):
        self._cards.extend(card_list)
    
    def card(self, index):
        return self._cards[index]
    
    def copy(self):
        deck = Deck (list (self._cards), self.deck_name, self.source_path)
        return deck
    
    def is_empty(self):
        return listutils.is_empty(self._cards)
    
    def is_not_empty(self):
        return not self.is_empty()

    def remove(self, index):
        if index < self.count:
            del self._cards[index]

    def shuffle(self):
        if self.is_not_empty():
            shuffle(self._cards)
        
    def sort(self):
        if self.is_not_empty():
            self._cards.sort(key=operator.attrgetter('title'))
