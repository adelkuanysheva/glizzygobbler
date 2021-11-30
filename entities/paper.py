import pygame
import random


class Paper(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        image = pygame.image.load('./photos/paper.png')
        self.image = pygame.transform.scale(image, (25, 25))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    
    def update(self):
    
        
        self.rect.y += 4

        if self.rect.y > 250 and len(self.groups()[0]) < 2:
            new_paper = Paper(random.randint(150, 700), 0)
            self.groups()[0].add(new_paper)

        if self.rect.y > 500:
            self.kill()
