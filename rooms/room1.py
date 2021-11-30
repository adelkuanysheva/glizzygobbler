import pygame
from entities import Wall
from .room import Room
from entities import Enemy, Collectable


WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Room1(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, WHITE],
                 [0, 350, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [150, 20, 20, 400, RED],
                 [300, 180, 20, 400, RED],
                 [450, 20, 20, 400, RED],
                 [600, 180, 20, 400, RED],
                 ]

        enemies = []

        collectables = [[350, 150],
                        [520, 380],
                        [40, 320],
                        [650, 490]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for item in enemies:
            enemy = Enemy(item[0], item[1])
            self.enemy_list.add(enemy)

        for item in collectables:
            collectable = Collectable(item[0], item[1])
            self.collectable_list.add(collectable)

