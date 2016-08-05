from ua.core.utils import strutils
from flashcards.card import Card

'''
    Converts text files with format
    Title            // Single line title
    Text...          // Multiline content 
    [blank...]       // Blank Line Break
'''

STATE_BREAK = 'break'
STATE_TITLE = 'title'
STATE_CONTENT = 'content'

class CardConvertorTextSmb:
    
    def read (self, file_path):
        
        lines = self._read_file (file_path)
        flashcards = self._from_lines(lines)
        
        return flashcards
    
    def _from_lines (self, lines):
        
        flashcards = []
        flashcard = None
        state = STATE_BREAK
    
        for line in lines:
           
            if (strutils.is_blank(line)):

                if state != STATE_BREAK:
                    state = STATE_BREAK
                    flashcards.append(flashcard)
                    flashcard = None
                    
                # Else:
                    # Ignore - just another break line. 
                
            else:
                
                if state == STATE_BREAK:
                    state = STATE_TITLE
                    flashcard = Card(title = line)
                    
                elif state == STATE_TITLE:
                    state = STATE_CONTENT
                    flashcard.content = line
                    
                else: # Must be a multiline description:
                    flashcard.content += '\n' + line
                    
        if flashcard:
            flashcards.append (flashcard)
        
        return flashcards
        
    
    def _read_file (self, file_path):
        
        with open(file_path) as file_handle:    # 'r' is optional
            lines = [line.rstrip('\n') for line in file_handle.readlines()]
        
        return lines
    
    
