from ua.core.utils.isfirst import IsFirst
class DecksView:
    
    def __init__(self, console, decks_model):
        
        self._console = console
        self._decks_model = decks_model
    
    def view_cards(self):
        
        is_first = IsFirst()
        
        self._console.clear_line()        
        
        for deck in self._decks_model.decks:
            
            if is_first.is_not_first():
                self._console.newline()
                
            self._console.print_line ("Deck:  " + deck.deck_name)
            self._console.newline()
            
            for card in deck.sorted_cards:
                self._console.print_line ("    " + card.title)
        
    def view_main (self):
        
        self._console.clear_line()        
        self._console.print_line ("- Flash Cards -")
        self._console.newline()
        
        for deck in self._decks_model.decks:
            self._console.print_line ("    " + deck.deck_name)
            
        self.view_main_options()
        
    def view_main_options(self):
        
        self._console.newline()
        self._console.print("Study, Study In Order, List Cards, Quit  [ Enter | Space | L | Q ]?")

    def view_quit_app(self):
        
        self._console.clear_line() 
        self._console.print_line ('Done.')
    
