import pygame
import requests

from .base import PygameView

class StartView(PygameView):
    """Main view for the game - draws a rectangle on the screen"""

    def draw(self):

        self.window.fill((250, 0, 0))
        self.image = pygame.image.load("./photos/startscreen.png")
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.window.blit(self.image, (0, 0))

        