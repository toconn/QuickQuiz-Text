from ua.core.utils import strutils

# Module Constants

KEY_CONTROL_C  = 'CONTROL C'
KEY_DELETE     = 'Del'
KEY_ENTER      = 'Enter'
KEY_LIST       = 'l'
KEY_QUIT       = 'q'
KEY_QUIT_APP   = 'X'
KEY_SPACE      = ' '

# Class Definition

class DecksControl:

    def __init__(self, console, decks_model, decks_view, play_deck_factory):

        self._console = console             # Used here to read in the keyboard.

        self._decks_model = decks_model
        self._decks_view = decks_view
        self._play_deck_factory = play_deck_factory
        
    def run(self):
        
        self._decks_view.view_main()         # 1st thing to display.
        
        while True:
            key = self._console.read_key()
            exit_app = self.process_next_input(key)
            if exit_app:
                return
    
    def process_next_input(self, key):
        
        exit_app = False
        
        if self._is_key (KEY_CONTROL_C, key) or \
           self._is_key (KEY_QUIT_APP, key):
            
            # Standard quit application keys:
            
            self._decks_view.view_quit_app()
            exit_app = True

        elif self._is_key (KEY_LIST, key):
            
            self._decks_view.view_cards()
            self._decks_view.view_main_options()
            
        elif self._is_key (KEY_ENTER, key):
            
            exit_app = self._play_deck (shuffle = True)
            
        elif self._is_key (' ', key):
            
            exit_app = self._play_deck (shuffle = False)             

        else:
            
            # Should never be able to get here.
            
            print ('Error: Process None!!!!')
            exit_app = True
        
        return exit_app

    def _new_play_deck_controller(self, shuffle):
        
        deck_model = self._decks_model.new_play_deck_model(shuffle)
        controller = self._play_deck_factory.new_play_deck_control(self._console, deck_model)
        
        return controller
    
    def _play_deck (self, shuffle):
        
        play_deck_controller = self._new_play_deck_controller(shuffle)
        exit_app = play_deck_controller.run()
        
        if not exit_app:
            self._console.clear_line()
            self._decks_view.view_main_options()
            
        return exit_app      
        
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

