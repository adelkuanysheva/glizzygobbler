import pygame
from controllers.base import PygameController



class StartController(PygameController):

    def __init__(self, view):
        """Constructor - sets variables"""
        super().__init__(view)


    def process(self, event):
        """
        This method overrides the parent's.
        Its job is to do something when the user clicks in the shape.
        """

        # First call the parent method, just in case we want to exit
        running = super().process(event)

        if running is False:
            raise UserWarning 

        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.K_RETURN:
                    return False

        return True