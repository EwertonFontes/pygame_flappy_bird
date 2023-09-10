import pygame
import random
from screen_elements import (
    ScreenElements, 
    TextElements, 
    PipeElements,
    CoinElements,
    BirdElements
)

class GameScene: 

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.coins_group = pygame.sprite.Group()
        self.pipes_group = pygame.sprite.Group()

        self.backgroud_image = ScreenElements("assets/sky.png", 0, 0, self.all_sprites)
        self.backgroud_image_aux = ScreenElements("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = ScreenElements("assets/ground.png", 0, 480, self.all_sprites)
        self.ground_aux = ScreenElements("assets/ground.png", 360, 480, self.all_sprites)
        
        self.score = TextElements("0", 100)
        self.bird = BirdElements("assets/bird0.png", 50, 320, self.all_sprites)

        self.ticks = 0
        self.change_scene = False
    
    def draw(self, window):
        self.all_sprites.draw(window) 
        self.score.draw(window, 150, 50)

    def update(self):
        self.move_bg()
        self.move_groud()
        self.all_sprites.update()
        if self.bird.play:
            self.spaw_pipes()
            self.bird.collision_coins(self.coins_group)
            self.bird.collision_pipes(self.pipes_group)
            self.score.update_text(str(self.bird.pts))    
        
    def move_bg(self):
        self.backgroud_image.rect[0] -= 1
        self.backgroud_image_aux.rect[0] -= 1

        if self.backgroud_image.rect[0] <= -360:
            self.backgroud_image.rect[0] = 0
        if self.backgroud_image_aux.rect[0] <= 0:
            self.backgroud_image_aux.rect[0] = 360
    
    def move_groud(self):
        self.ground.rect[0] -= 3
        self.ground_aux.rect[0] -= 3

        if self.ground.rect[0] <= -360:
            self.ground.rect[0] = 0
        if self.ground_aux.rect[0] <= 0:
            self.ground_aux.rect[0] = 360
    
    def spaw_pipes(self):
        self.ticks += 1

        if self.ticks >= random.randrange(60,110):
            self.ticks = 0
            pipe_down = PipeElements("assets/pipe1.png", 360, random.randrange(300,450), self.all_sprites, self.pipes_group)
            pipe_up = PipeElements("assets/pipe2.png", 360, pipe_down.rect[1] - 550, self.all_sprites, self.pipes_group)
            coin = CoinElements("assets/0.png", 386, pipe_down.rect[1] - 120, self.all_sprites, self.coins_group)

    
    def gameover(self):
        pass