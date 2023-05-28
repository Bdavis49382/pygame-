import pygame
KEY_BINDINGS = {
    pygame.K_w:'up',
    pygame.K_a:'left',
    pygame.K_s:'down',
    pygame.K_d:'right',
    pygame.K_UP:'up',
    pygame.K_LEFT:'left',
    pygame.K_RIGHT:'right',
    pygame.K_DOWN:'down'
}
TILE_SIZE = 64

MAP_COLUMNS = 16
MAP_ROWS = 10

BOTTOM_MARGIN = 0

SCREEN_WIDTH = MAP_COLUMNS * TILE_SIZE
SCREEN_HEIGHT = MAP_ROWS * TILE_SIZE + BOTTOM_MARGIN

GAME_TITLE = 'Seership'

DEFAULT_POS = (MAP_COLUMNS//2,MAP_ROWS//2)

TEXTURE_REFERENCE = "0x72_16x16DungeonTileset.v5/items/{0}.png"

DEBUG = False

SPRITE_SIZE = 16

MAP_KEY = {
    'floor':'floor_mud_e',
    'rocks':'rocks'
    }

DEFAULT_GAME_SCREEN = 'mine_entrance'

HARD_TILES = ['rocks']

SAVED_SERVERS = 'pygame++/multiplayer/saved_servers.csv'


BLACK = ( 0, 0, 0)
GRAY = (100,100,100)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

ENTRANCE = {'BOTTOM':(MAP_COLUMNS//2,MAP_ROWS-1),'TOP':(MAP_COLUMNS//2,0),'RIGHT':(MAP_COLUMNS-1,MAP_ROWS//2),'LEFT':(0,MAP_ROWS//2)}