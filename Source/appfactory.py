from argparse import ArgumentParser

from ua.core.ui.console import Console

import appconst
from flashapp.deckscontroller import DecksControl
from flashapp.decksview import DecksView
from flashapp.playdeckcontroller import PlayDeckControl
from flashapp.playdeckview import PlayDeckView
from flashcards.convertors.conv_factory import ConversionFactory
from flashcards.deckmodeldefault import DeckModelDefault
from flashcards.decksmodeldefault import DecksModelDefault
from flashcards.deckloader import DeckLoader


class PlayDeckFactory:
    
    def new_play_deck_control(self, console, deck_model):

        view = PlayDeckView(console, deck_model)
        control = PlayDeckControl(console, deck_model, view)
        
        return control

    def new_deck_model(self, deck, shuffle=False):

        return DeckModelDefault(deck, shuffle)


def new_argument_parser():
    
    parser = ArgumentParser(
        prog = appconst.APP_INFO.name,
        description = 'Creates an Python egg file from py source directories.',
        usage = appconst.HELP_USAGE,
        add_help=False
    )

    parser.add_argument('deck_paths', nargs='*', help='Path to Flash deck file.') # 

    parser.add_argument('-h', '--help', help='show this help message', action='store_true', dest='help_flag')        
    parser.add_argument('-p', '--parameters', help='show parameters', action='store_true', dest='params_flag')
    parser.add_argument('-v', '--version', help='show app version', action='store_true', dest='version_flag')
    
    return parser

def new_console():
 
    return Console()

def new_deck_loader():

    conv_factory = ConversionFactory()
    deck_loader = DeckLoader(conv_factory)
    
    return deck_loader

def new_decks_control(deck_paths):
 
    console = new_console()
    play_deck_factory = new_play_deck_factory()
    
    model = new_decks_model(deck_paths)
    view = DecksView(console, model)
    control = DecksControl(console, model, view, play_deck_factory)
    
    return control

def new_decks_model (deck_paths):
    
    deck_loader = new_deck_loader()
    play_deck_factory = new_play_deck_factory()
    
    decks_model = DecksModelDefault(deck_loader, deck_paths, play_deck_factory)
     
    return decks_model

def new_play_deck_factory():
    
    return PlayDeckFactory()
