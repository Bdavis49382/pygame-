from config import GRAY,TILE_SIZE
import pygame

class Game_screen:
    def __init__(self,screen,sprites,tilemaps,labels,background=GRAY) -> None:
        """A game screen made up of tilemaps, sprites, and labels
        screen: the pygame screen it will be drawn onto
        sprites: a group of sprites that will be updated and drawn
        tilemaps: a list of tilemaps NOTE even if you only have one tilemap for the whole screen,
        still put that tilemap into a list
        labels: a list of labels, like the tilemaps, must be in a list even if there is only one
        background: If you want to change the background from gray, enter RGB values here"""

        self.screen = screen
        self.background = background
        self.tilemaps = tilemaps
        self.labels = labels
        self.sprites = sprites
    
    def clicked(self):
        """Returns the node on the tile clicked on. If there is no node, it returns the tile_pos and value of the map on that tile in a dictionary."""
        [x,y] = pygame.mouse.get_pos()
        tile_pos = [x//TILE_SIZE,y//TILE_SIZE]
        for node in self.sprites:
            if node.tile_pos == tile_pos:
                return node
        return {'tile_pos':tile_pos,'tile':self.tilemaps[0].map[tile_pos[1]][tile_pos[0]]}

    def draw(self):
        """Draws all the elements of the game_screen onto the pygame screen"""
        self.screen.fill(self.background)

        for tilemap in self.tilemaps:
            tilemap.draw()
        
        self.sprites.update()
        self.sprites.draw(self.screen)

        for label in self.labels:
            label.draw()
        
        pygame.display.flip()
