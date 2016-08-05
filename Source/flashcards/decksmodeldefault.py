from flashcards.deck import Deck
from flashcards.decksmodel import DecksModel

class DecksModelDefault(DecksModel):

    def __init__ (self, deck_loader, deck_paths, play_deck_factory):
        
        self._decks = []
        self._deck_loader = deck_loader
        self._deck_paths = deck_paths
        self._play_deck_factory = play_deck_factory
        self._load_decks()
        
    @property
    def card_count(self):

        if self.deck_count() > 0:
            count = sum (deck.count for deck in self._decks)
        else:
            count = 0
            
        return count
        
    @property
    def deck_count(self):

        if self._decks:
            count = self._decks.count
        else:
            count = 0
            
        return count
        
    @property
    def deck_names(self):
        return self._deck_names
    
    @property
    def decks(self):
        
        decks = [ deck.copy() for deck in self._decks ]
        
        return decks

    def deck(self, index):
        
        if index < self.deck_count():
            deck = self._decks[index]
        else:
            deck = None
        
        return deck
    
    def new_play_deck_model(self, shuffle):
        
        cards = []
        for deck in self._decks:
            if deck.enabled:
                cards.extend(deck.cards)

        deck = Deck(cards) 
        deck_model = self._play_deck_factory.new_deck_model(deck, shuffle)
        
        return deck_model
    
    def _load_decks(self):
        
        for deck_path in self._deck_paths:
            deck = self._deck_loader.load_deck (deck_path)
            self._decks.append (deck)

