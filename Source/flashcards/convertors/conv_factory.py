from flashcards.flashcard_consts import *
from flashcards.convertors.conv_text_smb import CardConvertorTextSmb

class ConversionFactory:

    def create_convertor (self, type=convert_type_default):
    
        if type == convert_type_text_smb:
            convertor = CardConvertorTextSmb()
        else:
            convertor = CardConvertorTextSmb()
            
        return convertor
