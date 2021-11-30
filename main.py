import pygame

from views import StartView
from controllers import StartController, End
from views.end import EndView
from views.maze import MazeView
from models import Game
from entities import Explosion

 
def main():
    """ Main Program """
 
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    start_view = StartView(screen)
    start = StartController(start_view)
    try:
        start.run()
    except UserWarning:
        pygame.quit()

    game = Game()
    maze_view = MazeView(game, screen)


    running = True

    while running:

        maze_view.draw()
        maze_view.update()

        game.explosions.draw(screen)
        game.explosions.update()
        
        # Block moving

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.block.changespeed(-10, 0)
                    game.block.image = game.block.flip("left")
                if event.key == pygame.K_RIGHT:
                    game.block.changespeed(10, 0)
                    game.block.image = game.block.flip("right")
                if event.key == pygame.K_UP:
                    game.block.changespeed(0, -10)
                if event.key == pygame.K_DOWN:
                    game.block.changespeed(0, 10)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    game.block.changespeed(10, 0)
                if event.key == pygame.K_RIGHT:
                    game.block.changespeed(-10, 0)
                if event.key == pygame.K_UP:
                    game.block.changespeed(0, 10)
                if event.key == pygame.K_DOWN:
                    game.block.changespeed(0, -10)

        game.block.move(game.current_room.wall_list)
 

 
        if game.block.rect.x < -15:
            if game.current_room_num == 0:
                game.current_room_num = 2
                game.current_room = game.rooms[game.current_room_num]
                game.block.rect.x = 790
            elif game.current_room_num == 2:
                game.current_room_num = 1
                game.current_room = game.rooms[game.current_room_num]
                game.block.rect.x = 790
            else:
                game.current_room_num = 0
                game.current_room = game.rooms[game.current_room_num]
                game.block.rect.x = 790
 
        if game.block.rect.x > 801:
            if game.current_room_num == 0:
                game.current_room_num = 1
                game.current_room = game.rooms[game.current_room_num]
                game.block.rect.x = 0
            elif game.current_room_num == 1:
                game.current_room_num = 2
                game.current_room = game.rooms[game.current_room_num]
                game.block.rect.x = 0
            else:
                running = False
                game.message = "You WON!"


        for game.enemy in game.current_room.enemy_list:
            screen.blit(game.enemy_image, game.enemy.rect)
            game.enemy.update()

        for game.paper in game.current_room.paper_list:
            screen.blit(game.paper_image, game.paper.rect)
            game.paper.update()

        for game.collectable in game.current_room.collectable_list:
            screen.blit(game.collectable_image, game.collectable.rect)

        if pygame.sprite.groupcollide(game.movingsprites,
                                        game.current_room.enemy_list,
                                        False, True):
                running = False

        if pygame.sprite.groupcollide(game.movingsprites,
                                                game.current_room.paper_list,
                                                False, True):

                    explosion = Explosion(game.block.rect.x, game.block.rect.y)
                    game.explosions.add(explosion)
                    game.score += 500
                    running = True
                    game.current_room.enemy_list.remove(game.block.find(game))


        if pygame.sprite.groupcollide(game.movingsprites,
                                        game.current_room.collectable_list,
                                        False, True):
            game.score += 100
            print('Your score is: ', game.score)
        
        pygame.display.update()


    end_view = EndView(screen, score=game.score, message=game.message)
    end = End(end_view)
    end.run()
 

 
if __name__ == "__main__":
    main()