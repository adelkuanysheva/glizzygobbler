import pygame

from entities import Block, Enemy, Collectable, Paper
from rooms import Room1, Room2, Room3

class Game: 

    def __init__(self):

        self.block = Block(50, 260)
        self.increment = 3
        self.block_image = self.block.image
    
        self.movingsprites = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.movingsprites.add(self.block)
    
        self.rooms = []
        self.score = 0
        self.enemy = Enemy(50, 200)
        self.enemy_image = self.enemy.image
        self.paper = Paper(50, 210)
        self.paper_image = self.paper.image
        self.collectable = Collectable(40, 40)
        self.collectable_image = self.collectable.image
        self.message = "You LOST!"
    
        self.room1 = Room1()
        self.rooms.append(self.room1)
    
        self.room2 = Room2()
        self.rooms.append(self.room2)
    
        self.room3 = Room3()
        self.rooms.append(self.room3)
 
        self.current_room_num = 0
        self.current_room = self.rooms[self.current_room_num]
