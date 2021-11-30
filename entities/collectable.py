import pygame


class Collectable(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        image = pygame.image.load('./photos/hotdog.png')
        self.image = pygame.transform.scale(image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self, screen, game):

        screen.blit(game.collectable_image, game.collectable.rect)