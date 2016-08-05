class Card:
    
    def __init__ (self, content=None, title=None):
        
        self.content = content
        self.title = title 
        
    def __repr__ (self):
        
        return "Flashcard [" + self.title + ", " + self.content + "]"
