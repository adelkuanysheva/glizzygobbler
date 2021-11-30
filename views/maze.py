import pygame
from .base import PygameView


class MazeView(PygameView):

    def __init__(self, maze, window):
        super().__init__(window)
        self.maze = maze
        self.font = pygame.font.SysFont("monospace", 32)

    def draw(self): 

        self.window.fill((0,0,0))
        self.maze.movingsprites.draw(self.window)

        self.maze.current_room.wall_list.draw(self.window)
        self.maze.current_room.enemy_list.draw(self.window)
        self.maze.current_room.collectable_list.draw(self.window)
        self.window.blit(self.maze.block.image, self.maze.block.rect)
        score_text = self.render_text_surface("SCORE : " + str(self.maze.score))
        self.window.blit(score_text, (25, 550))

        pygame.display.flip()
    
        