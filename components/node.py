from config import WHITE,TILE_SIZE,DEFAULT_POS,TEXTURE_REFERENCE,SPRITE_SIZE,KEY_BINDINGS,SCREEN_HEIGHT,SCREEN_WIDTH,HARD_TILES
import pygame
class Node(pygame.sprite.Sprite):

    def __init__(self,type,name='',tile_pos=DEFAULT_POS,filename='',tile_size=TILE_SIZE) -> None:
        """A node is an object on the screen. An extension of pygame.sprite, it uses a tile-based system and a 
        texture reference from the config to create an object which can be drawn on the screen.
        type: the type of object is is, EX: item, enemy, player
        name: the name of the specific object, if necessary
        tile_pos: the x and y position by tiles of the object. Takes a default position from the config file
        file_name: the name of the specific file for the texture. NOTE: Doesn't require the whole path. Uses TEXTURE_REFERENCE
        from the config file.
        tile_size: if the tile_size needs to be different from the config file for any reason, this can be changed here"""
        super().__init__()

        self.tile_size = tile_size
        self.type = type
        self.name = name

        self.file_name = filename
        self.tile_pos = tile_pos

        self.load_image(filename)

    
    def load_image(self,filename):
        if filename != '':
            if ':' in filename:
                self.image = pygame.image.load(TEXTURE_REFERENCE.format(filename.split(':')[0])).convert_alpha()
                rect = pygame.Rect(int(filename.split(':')[1])*SPRITE_SIZE,0,SPRITE_SIZE,SPRITE_SIZE)
                image = pygame.Surface(rect.size).convert()
                image.blit(self.image,(0,0), rect)
                self.image = image
            else:
                self.image = pygame.image.load(TEXTURE_REFERENCE.format(filename)).convert_alpha()

            self.image = pygame.transform.scale(self.image, (self.tile_size,self.tile_size))
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.Surface([self.tile_size,self.tile_size])
            self.image.fill(WHITE)
            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
        self.rect.x = self.tile_pos[0]*self.tile_size
        self.rect.y = self.tile_pos[1]*self.tile_size

    def get_collisions(self,new_x,new_y,sprite_group):
        collisions = []
        for node in sprite_group:
            if node.tile_pos[0] == new_x and node.tile_pos[1] == new_y:
                collisions.append(node)
        return collisions
        
    def can_move(self,new_x,new_y,tilemap,sprite_group):
        if new_x < 0 or new_y < 0 or new_x * self.tile_size >= tilemap.size[0] * self.tile_size or new_y * self.tile_size >= tilemap.size[1] * self.tile_size:
            return False
        if tilemap.map[new_y][new_x] in HARD_TILES:
            return False
        collisions = self.get_collisions(new_x,new_y,sprite_group)
        if len(collisions):
            self.collide_with(collisions)
            return False
        return True
    

    def move(self,direction,tilemap,sprite_group):
        """Moves the node one tile in the chosen direction.
         direction: a string or pygame key representing the direction. If given a pygame key will use config KEY_BINDINGS
         tilemap: the tilemap the node is currently on. If HARD_TILES are in the config, nodes cannot go over those tiles
         sprite_group: whatever sprite group has other nodes this node could collide with"""
        if type(direction) == int and direction in KEY_BINDINGS.keys():
            direction = KEY_BINDINGS[direction]
        new_x = self.tile_pos[0]
        new_y = self.tile_pos[1]
        match (direction):
            case 'left':
                new_x -= 1
            case 'right':
                new_x += 1
            case 'up':
                new_y -= 1
            case 'down':
                new_y += 1
        
        if self.can_move(new_x,new_y,tilemap,sprite_group): 
            self.tile_pos = (new_x,new_y)
            self.rect.x = new_x*self.tile_size
            self.rect.y = new_y*self.tile_size
    
    def __str__(self) -> str:
        return f'type:{self.type}, texture:{self.file_name}, position:{self.tile_pos}'

    # An inherited class could replace this function with any code to deal with the collisions
    def collide_with(self,collisions):
        pass

