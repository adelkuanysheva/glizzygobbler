import pygame

class Block(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """
 
    # Set speed vector
    change_x = 0
    change_y = 0
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.image.load('./photos/tim.png')
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.flipped = pygame.transform.flip(self.image, True, False)
 
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls):
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


    def flip(self, direction):
        
        if direction == "left":
            self.image = self.flipped
        if direction == "right":
            self.image = pygame.image.load('./photos/tim.png')
            self.image = pygame.transform.scale(self.image, (60, 60))
        return self.image


    def find(self, game):

        pos = pygame.math.Vector2(self.rect.x, self.rect.y)
        enemy = min([e for e in game.current_room.enemy_list], 
                key=lambda e: pos.distance_to(pygame.math.Vector2(e.rect.x, e.rect.y)))

        if enemy == []:
            return None
        else: 
            return enemy