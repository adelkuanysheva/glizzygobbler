import pygame 

import os
import sys

from .base import PygameController


class End(PygameController):
    """Win controller: just waits for escape / closing the window"""

    def process(self, event):
        """Abstract method: should be implemented by child classes"""
        # Invoked close from the OS
        if event.type == pygame.locals.QUIT:
            return False
        # Pressed a key - is it Escape?
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                return False
            if event.key == pygame.locals.K_SPACE:
                os.execl(sys.executable, *([sys.executable] + sys.argv))

        return True