import pygame
from entities import Wall
from .room import Room
from entities import Enemy, Collectable, Paper

WHITE = (255, 255, 255)
RED = (255, 0, 0)



class Room3(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, WHITE],
                 [0, 370, 20, 250, WHITE],
                 [780, 0, 20, 250, WHITE],
                 [780, 350, 20, 250, WHITE],
                 [20, 0, 760, 20, WHITE],
                 [20, 580, 760, 20, WHITE],
                 [0, 230, 150, 20, RED],
                 [0, 350, 150, 20, RED]]

        enemies = [[400, 190],
                   [500, 390],
                   [600, 590],
                   [300, 290],
                   [200, 690]]

        
        papers = [[400, 190],
                   [450, 39],
                   [500, 500],
                   [750, 100],
                   [700, 690]]


        collectables = [[40, 40],
                        [30, 400],
                        [400, 400],
                        [400, 100]]


        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for item in enemies:
            enemy = Enemy(item[0], item[1])
            self.enemy_list.add(enemy)

        for item in papers:
            paper = Paper(item[0], item[1])
            self.paper_list.add(paper)

        for item in collectables:
            collectable = Collectable(item[0], item[1])
            self.collectable_list.add(collectable)


