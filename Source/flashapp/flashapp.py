import appfactory

class FlashApp:
    
    def __init__ (self, deck_paths):
        
        self._decks_controller = appfactory.new_decks_control(deck_paths)

    def run(self):

        self._decks_controller.run()
        