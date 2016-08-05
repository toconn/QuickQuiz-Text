from flashcards.deckmodel import DeckModel

# Module Constants:

STATE_QUESTION = 1
STATE_ANSWER = 2
STATE_END_OF_DECK = 3

# Module Class

class DeckModelDefault(DeckModel):

    def __init__ (self, deck, shuffle=False):
        
        self._current_card = None   # Using this to prevent problems with empty deck or removing a card from the deck.
        self._deck = deck
        self._is_shuffled = shuffle
        self._state = STATE_QUESTION
        
        self.reset_deck()
        
    @property
    def count(self):
        return self._deck.count
        
    @property
    def cards(self):        
        return list(self._deck.cards)

    @property
    def current_card(self):
        return self._current_card
        
    @property
    def current_card_number(self):
        return self._current_index + 1

    @property   
    def is_answer(self):
        return self._state == STATE_ANSWER

    @property   
    def is_end_of_deck(self):
        return self._state == STATE_END_OF_DECK

    @property   
    def is_question(self):
        return self._state == STATE_QUESTION

    @property
    def sorted_cards(self):
        return self._deck.sorted_cards


    def card(self, index):
        return self._deck.card(index)
    
    def copy(self):
        return DeckModelDefault(self._deck.copy())

    def current_answer(self):
        '''Sets the state to answer and returns the answer.
        '''
        
        if self._current_card is not None:
            self._state = STATE_ANSWER
            return self._current_card.content
        else:
            return ""
        
    def current_question(self):
        '''Sets the state to question and returns the question.
        '''
        
        if self._current_card is not None:
            self._state = STATE_QUESTION
            return self._current_card.title
        else:
            return ""
        
    def next_card(self):
        
        if self._has_next():
            self._current_index = self._current_index + 1
            self._current_card = self._deck.card(self._current_index)
            self._state = STATE_QUESTION
        else:
            self._current_card = None
            self._state = STATE_END_OF_DECK
            
        return self._current_card

    def remove_current_card(self):
        
        if self._current_card is not None and self._deck.is_not_empty() and self._current_index < self.count:
            
            self._deck.remove(self._current_index)
            self._current_card = None
            self._current_index = self._current_index - 1
            self._state = STATE_ANSWER

    def reset_deck(self):
        ''' Resets the deck.
            If the deck was shuffled before, reshuffle the deck.
            Returns the first card off the deck.
        '''
        
        if self._is_shuffled:
            self._deck.shuffle()

        self._reset_current_index()
        
        return self.next_card()
        
    def shuffle(self):
        self._deck.shuffle()
        
    def sort(self):
        self._deck.sort()

    def _has_next(self):
        return self._current_index < self.count - 1
    
    def _reset_current_index(self):
        self._current_index = -1
        self._state = STATE_QUESTION

