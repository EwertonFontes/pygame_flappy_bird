
from typing import Any
import pygame


class ScreenElements(pygame.sprite.Sprite):
    def __init__(self, image, axis_x, axis_y, *groups):
        super().__init__(*groups)
        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = axis_x
        self.rect[1] = axis_y

        self.frame = 1
        self.tick = 0

    def draw(self, window):
        pass

    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()

    def animation(self, image: str, amount_images: int):
        self.ticks = (self.ticks + 1) % amount_images # quantidade de imagem do obj
        self.image = pygame.image.load(f"assets/{image}{str(self.ticks)}.png")   
 

class PipeElements(ScreenElements):
    def __init__(self, image, axis_x, axis_y, *groups):
        super().__init__(image, axis_x, axis_y, *groups)

    def update(self, *args):
        self.move()


class CoinElements(ScreenElements):
    def __init__(self, image, axis_x, axis_y, *groups):
        super().__init__(image, axis_x, axis_y, *groups)
        self.ticks = 0
    
    def update(self, *args):
        self.move()
        self.animation(image="", amount_images=6)

class BirdElements(ScreenElements):
    def __init__(self, image, axis_x, axis_y, *groups):
        super().__init__(image, axis_x, axis_y, *groups)
        
        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound("assets/sounds/point.ogg")
        self.sound_block = pygame.mixer.Sound("assets/sounds/hit.ogg")
        self.sound_wing = pygame.mixer.Sound("assets/sounds/wing.ogg")

        self.ticks = 0
        self.speed = 4
        self.gravity = 1

        self.play = True
        self.pts = 0

    def update(self, *args):
        self.animation(image="bird", amount_images=4)
        self.move_bird()

    def move_bird(self):
        key = pygame.key.get_pressed()
        self.speed += self.gravity
        self.rect[1] += self.speed

        if self.speed >= 15:
            self.speed = 15
       
        if self.play:
            if key[pygame.K_SPACE]:
                self.speed -=5
                self.sound_wing.play()
        
        if self.rect[1] >= 440:
            self.rect[1] = 440
        elif self.rect[1] <= 0:
            self.rect[1] = 0
            self.speed = 4

    def collision_pipes(self, group):
        collide = pygame.sprite.spritecollide(self, group, False)
        if collide:
            self.sound_block.play()
            self.play = False

    def collision_coins(self, group):
        collide = pygame.sprite.spritecollide(self, group, True)
        if collide:
            self.sound_pts.play()
            self.pts += 1

class TextElements:
    text_screen: str
    size: int

    def __init__(self, text_screen, size):
        self.font = pygame.font.Font("assets/font/font.ttf", size)
        self.render = self.font.render(text_screen, True, (255,255,255))
    
    def draw(self, window, axis_x, axis_y):
        window.blit(self.render, (axis_x, axis_y))
    
    def update_text(self, text_screen):
        self.render = self.font.render(text_screen, True, (255,255,255))