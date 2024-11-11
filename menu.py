import pygame

class Menu:
    def __init__(self,menu_img):
        self.menu=pygame.image.load(menu_img).convert_alpha()