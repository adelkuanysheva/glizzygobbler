import pygame
from entities import Wall
from .room import Room
from entities import Enemy, Collectable


WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Room2(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, WHITE],
                 [0, 370, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [0, 230, 150, 20, RED],
                 [0, 350, 150, 20, RED],
                 [200, 150, 150, 20, RED],
                 [200, 450, 150, 20, RED],
                 [350, 150, 20, 160, RED],
                 [350, 310, 20, 160, RED],
                 [450, 0, 20, 160, RED],
                 [450, 410, 20, 160, RED]]


        enemies = [[500, 190],
                   [600, 390],
                   [700, 590]]


        collectables = [[375, 150],
                        [550, 380],
                        [400, 400]]


        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for item in enemies:
            enemy = Enemy(item[0], item[1])
            self.enemy_list.add(enemy)


        for item in collectables:
            collectable = Collectable(item[0], item[1])
            self.collectable_list.add(collectable)


