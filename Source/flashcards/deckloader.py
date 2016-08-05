from ua.core.utils import fileutils
from flashcards.deck import Deck

class DeckLoader:

    def __init__ (self, conv_factory):
        
        self._conv_factory = conv_factory
    
    def load_deck (self, file_path):
        
        convertor = self._conv_factory.create_convertor()
        cards = convertor.read (file_path)
        deck = Deck (cards, self.get_deck_name (file_path), file_path)
        
        return deck
    
    def get_deck_name (self, file_path):
        
        return fileutils.path_file_name(file_path)