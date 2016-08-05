from ua.core.utils import fileutils
from ua.core.utils import listutils
from flashapp.flashapp import FlashApp
import apputils


class App:
    
    def main (self, parsed_params):
        
        if listutils.is_not_empty(parsed_params.deck_paths):
            
            deck_paths = parsed_params.deck_paths
            
            deck_paths = self._normalize_deck_paths(deck_paths)
            errors = self._validate_decks(deck_paths)

            if errors is None:

                print('')
                flash_app = FlashApp(deck_paths)
                flash_app.run()
                
            else:
                
                [ print(error) for error in errors ]
            
            print('')
            
    def show_help(self):
        
        self._argument_parser.print_help()
        print ('')

    def show_params(self, parsed_params):
        
        apputils.show_params(parsed_params)
    
    def show_version(self):
        
        apputils.show_version(self._app_info)
        
    def _normalize_deck_paths(self, deck_paths):
        
        normalized_deck_paths = []
        
        for deck_path in deck_paths:
            if not fileutils.has_dir_in_path(deck_path):
                normalized_deck_paths.append(fileutils.add_cwd_to_file_name(deck_path))
            else:
                normalized_deck_paths.append(deck_path)
            
        return normalized_deck_paths
        
    def _validate_decks(self, deck_paths):
        
        error_list = []
        
        for deck_path in deck_paths:
            if not fileutils.is_file_exists(deck_path):
                error_list.append("File not found: " + deck_path)
        
        if len(error_list) > 0:
            return error_list
        else:
            return None

