import abc

class FlashcardConvertor:
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def read (self, file_path):
        ''' Returns a list of flash cards.
        '''
        return
