import pygame
import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        image = pygame.image.load('./photos/anvil.png')
        self.image = pygame.transform.scale(image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x



    def update(self):

        self.rect.y += 3

        if self.rect.y > 250 and len(self.groups()[0]) < 2:
            new_enemy = Enemy(random.randint(300, 700), 0)
            self.groups()[0].add(new_enemy)

        if self.rect.y > 500:
            self.kill()
