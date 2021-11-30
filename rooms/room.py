import pygame

class Room(object):

    wall_list = None
    enemy_list = None
    paper_list = None
    collectable_list = None


    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.paper_list = pygame.sprite.Group()
        self.collectable_list = pygame.sprite.Group()
        