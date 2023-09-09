import pygame
import random
from screen_elements import ScreenElements, TextElements

class GameScene: 

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.backgroud_image = ScreenElements("assets/sky.png", 0, 0, self.all_sprites)
        self.backgroud_image_aux = ScreenElements("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = ScreenElements("assets/ground.png", 0, 480, self.all_sprites)
        self.ground_aux = ScreenElements("assets/ground.png", 360, 480, self.all_sprites)
        self.change_scene = False
    
    def draw(self, window):
        self.all_sprites.draw(window) 

    def update(self):
        self.move_bg()
        self.move_groud()
        self.all_sprites.update()

    
    def move_bg(self):
        self.backgroud_image.rect[0] -= 1
        self.backgroud_image_aux.rect[0] -= 1

        if self.backgroud_image.rect[0] <= -360:
            self.backgroud_image.rect[0] = 0
        if self.backgroud_image_aux.rect[0] <= 0:
            self.backgroud_image_aux.rect[0] = 360
    
    def move_groud(self):
        self.ground.rect[0] -= 2
        self.ground_aux.rect[0] -= 2

        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0
        if self.ground_aux.rect[0] <= 0:
            self.ground_aux.rect[0] = 360

    def gameover(self):
        pass