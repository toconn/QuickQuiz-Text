from ua.core.utils import strutils

# Module constants:

KEY_CONTROL_C  = 'CONTROL C'
KEY_DELETE     = 'Del'
KEY_ENTER      = 'Enter'
KEY_LIST       = 'l'
KEY_QUIT       = 'q'
KEY_QUIT_APP   = 'X'
KEY_SPACE      = ' '

# Class def:

class PlayDeckControl:

    def __init__(self, console, deck_model, play_deck_view):

        self._console = console                # Used here to read in the keyboard.

        self._deck_model = deck_model
        self._play_deck_view = play_deck_view
        
    def run(self):
        
        self._play_deck_view.view_card_question()    # 1st thing to display.
        
        while True:
            key = self._console.read_key()
            exit_app, exit_view = self.process_next_input(key)
            if exit_app or exit_view:
                return exit_app
    
    def process_next_input(self, key):
        
        exit_app = False
        exit_view = False
        
        if self._is_key (KEY_CONTROL_C, key) or \
           self._is_key (KEY_QUIT_APP, key):
            
            # Standard quit application keys:
            
            self._play_deck_view.view_quit_app()
            exit_app = True
                
        elif self._is_key (KEY_QUIT, key):
            
                # Quit from study mode....
                
                exit_view = True
                
        elif self._deck_model.is_answer:
            
            if self._is_key_enter_or_space(key):
                
                self._deck_model.next_card()
                self._play_deck_view.view_card_question()
                
            elif self._is_key (KEY_DELETE, key):
                
                self._deck_model.remove_current_card()
                self._deck_model.next_card()
                self._play_deck_view.view_card_question()          
            
        elif self._deck_model.is_question:
        
            if self._is_key_enter_or_space(key):
                
                self._deck_model.current_answer()   # Moves state along. Doesn't do anything else.
                self._play_deck_view.view_card_answer()
                
            elif self._is_key (KEY_DELETE, key):
                
                self._deck_model.remove_current_card()
                self._deck_model.next_card()
                self._play_deck_view.view_card_question()           
            
        elif self._deck_model.is_end_of_deck:
            
            if self._is_key_enter_or_space(key):
                
                self._deck_model.reset_deck()
                self._play_deck_view.view_card_question()
                
            if self._is_key (KEY_LIST, key):
                
                self._deck_model.view_cards()
                self._play_deck_view.view_card_options()
                                
        else:
            
            # Should never be able to get here.
            
            print ('Error: Process None!!!!')
            exit_app = True
        
        return exit_app, exit_view
    
    def _is_key (self, test_key, actual_key):
        
        if test_key is KEY_CONTROL_C:
            return ord(actual_key) == 3
        elif test_key is KEY_ENTER:
            return ord(actual_key) == 13
        elif test_key is KEY_DELETE:
            return ord(actual_key) == 127
        else:
            # print ("key " + repr(test_key) + ", " + repr(actual_key))
            return strutils.equals_ignore_case (test_key, actual_key)        
        
    def _is_key_enter_or_space(self, key):
        
        return self._is_key (KEY_ENTER, key) or self._is_key (KEY_SPACE, key)

