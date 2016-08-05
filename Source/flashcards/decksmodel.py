import abc

class DecksModel:
    ''' The base model for all FlashDecksModel classes.
    '''
    
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    @property
    def card_count(self):
        pass
    
    @abc.abstractproperty
    @property
    def deck_count(self):
        pass
    
    @abc.abstractproperty
    @property
    def deck_names(self):
        pass

    @abc.abstractproperty
    def deck (self, index):
        pass
    
    @abc.abstractproperty
    def new_play_deck_model(self):
        ''' returns a flash deck model with cards from the enabled decks.
        '''
        pass
    
    @abc.abstractproperty
    def refresh_decks(self):
        ''' refreshes the contents of the loaded decks from their source files.
        '''
        pass
