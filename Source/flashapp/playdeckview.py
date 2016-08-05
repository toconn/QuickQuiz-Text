class PlayDeckView:
    
    def __init__(self, console, flash_model):
        
        self._console = console
        self._deck_model = flash_model

    def view_card_answer(self):
    
        self._console.clear_line()
        self._console.print_line (self._deck_model.current_card.content)
        
        self.view_card_options()
        
    def view_card_options(self):
    
        self._console.newline()
        self._console.print(self._card_position() + "Next, Remove, Menu  [ Space | Del | Q ]?")
        
    def view_card_question(self):
        
        if self._deck_model.is_end_of_deck:
            self.view_play_end()
        else:
            self._console.clear_line()
            self._console.newline()
            self._console.print_line (self._deck_model.current_card.title)
            
            self.view_card_options()
    
    def view_card_removed (self):
        
        self._console.clear_line()
        self._console.print_line ("Card removed.")
        
    def view_cards(self):
        
        self._console.clear_line()        
        self._console.print_line ("Cards:")
        self._console.newline()
        
        for card in self._deck_model.sorted_cards():
            self._console.print_line ("    " + card.title)
        
    def view_quit_app(self):
        
        self._console.clear_line() 
        self._console.print_line ('Done.')
    
    def view_play_end (self):
        
        self._console.clear_line()
        self._console.newline()      
        self._console.print_line("- End of Deck -")
        
        self.view_play_end_options()           

    def view_play_end_options (self):
        
        self._console.newline()
        self._console.print("Again, List, Menu  [ Space | L | Q ]?")            

    def _card_position(self):
        return str(self._deck_model.current_card_number) + "/" + str(self._deck_model.count) + ": "
    
