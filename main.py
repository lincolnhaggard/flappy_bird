import pygame 
import sys
from game import Game

pygame.init()
screen=pygame.display.set_mode((400, 720))
clock=pygame.time.Clock()
game=Game("img/bird.png", "img/pipe.png","img/background.png","img/ground.png")
game.resize_images()

move=True
move2=True
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.show_background(screen)
    game.show_player(screen)
    game.update()
    pygame.display.update()
    clock.tick(120)