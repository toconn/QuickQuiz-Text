import abc

class DeckModel:
    ''' The base model for all FlashModel classes.
    '''
    
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    @property
    def card_count(self):
        pass

    @abc.abstractproperty
    @property
    def cards(self):
        pass

    @abc.abstractproperty
    @property   
    def current_card(self):
        pass
    
    @abc.abstractproperty
    @property   
    def current_card_number(self):
        pass
    
    @abc.abstractproperty
    @property   
    def is_answer(self):
        pass
    
    @abc.abstractproperty
    @property   
    def is_end_of_deck(self):
        pass
    
    @abc.abstractproperty
    @property
    def is_question(self):
        pass
    
    @abc.abstractproperty
    @property
    def sorted_cards(self):
        pass


    @abc.abstractmethod
    def card(self, index):
        pass

    @abc.abstractmethod
    def current_answer(self):
        pass
    
    @abc.abstractmethod
    def current_question(self):
        pass
      
    @abc.abstractmethod  
    def reset_deck(self):
        pass
    
    @abc.abstractmethod 
    def next_card(self):
        pass

    @abc.abstractmethod
    def remove_current_card(self):
        pass
    
    @abc.abstractmethod
    def shuffle(self):
        pass
    
    @abc.abstractmethod
    def sort(self):
        pass
