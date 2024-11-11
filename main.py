import pygame 
import sys
from game import Game

pygame.init()
screen=pygame.display.set_mode((400, 720))
clock=pygame.time.Clock()
game=Game("img/bird.png", "img/pipe.png","img/background.png","img/ground.png")
game.resize_images()
SPAWNPIPE = pygame.USEREVENT 
pygame.time.set_timer(SPAWNPIPE, int(2200.0/game.speed))






while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game.active:
                game.flap()

        if event.type==SPAWNPIPE:
            game.add_pipe()
    
    game.show_background(screen)
    game.show_ground(screen)
    game.show_pipe(screen)
    
    game.show_pipe(screen)
    game.show_bird(screen)
    if game.active: 
        
        game.update_bird()
        game.move_ground()
        game.move_pipes()
        game.check_collision()
    pygame.display.update()
    clock.tick(120)