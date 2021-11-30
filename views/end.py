from .base import PygameView

class EndView(PygameView):
    """View when the game is won"""

    def __init__(self, view, score, message):
        super().__init__(view)
        self.score = score
        self.message = message

    def draw(self):

        self.window.fill((0, 0, 0))
        text = self.render_text_surface(self.message)
        self.window.blit(text, (330, 100))

        game_over = self.render_text_surface(f" Your score: {self.score}")
        self.window.blit(game_over, (300, 350))
        
        restart = self.render_text_surface("Press Space Bar to restart")
        quit = self.render_text_surface("Press Esc to quit")

        self.window.blit(restart, (240, 255))
        self.window.blit(quit, (300, 300))

 