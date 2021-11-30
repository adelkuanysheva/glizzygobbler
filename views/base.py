from abc import ABC, abstractmethod

import pygame
import pygame.font


class PygameView(ABC):
    """Abstract class for a basic Pygame view"""

    def __init__(self, window):
        """Constructor receives a window (where everything will be displayed)"""
        self.window = window

    def render_text_surface(self, text):
        """Utility function to render a text surface"""
        font = pygame.font.SysFont("monospace", 32)
        text_surface = font.render(text, True, (255, 255, 255))

        return text_surface

    @abstractmethod
    def draw(self):
        """Child classes MUST implement the draw method"""
        raise NotImplementedError

    def update(self):
        """Update the screen"""
        pygame.display.flip()
