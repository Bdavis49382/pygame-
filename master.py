import pygame
from screens.ui import UI

class Master():
    """This is the interface or template for the master, or game clock of the game. It has the following attributes and
      functions which should be replaced by the actual master unless stated otherwise:
    all_sprites: a pygame sprite group which holds all the nodes being used in the game
    UI: a UI object 
    current_game_screen: a string which must be a game screen key recognized by the UI
    __init__(): THIS FUNCTION WILL NOT BE REPLACED. It will create the above attributes and prepare and start the game,
        so in order to start the game, simply create the Master object
    start_game(): THIS FUNCTION WILL NOT BE REPLACED. It is the game clock which calls other functions which you will change
    prepare_game(): a function which should contain any code preparing the game before the clock starts
    handle_event(event): a function to handle any events the game comes across. At the end of your function, return the super call of this function, as it contains code to quit the game.
    """
    def __init__(self) -> None:
        self.all_sprites = pygame.sprite.Group()
        self.current_game_screen = ''
        self.prepare_game()
        self.start_game()
    

    def start_game(self):
        playing = True
        while playing:
            self.UI.game_screens[self.current_game_screen].draw()
            
            for event in pygame.event.get():
                playing = self.handle_event(event)

    #These functions are meant to be replaced
    def prepare_game(self):
        """Prepares the game before the clock starts. At minimum it must create a UI"""
        self.UI = UI()
    
    #Use the super for this one.
    def handle_event(self,event):
        """Handles every event that the game clock comes across"""
        if event.type==pygame.QUIT:
            return False
        else:
            return True
