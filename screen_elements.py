
import pygame


class ScreenElements:
    image: str
    axis_x: int
    axis_y: int

    def __init__(self, image, axis_x, axis_y):
        
        #Informação de um  grupo de elemento
        self.group = pygame.sprite.Group()
        #images, dimensões, tamanhos
        self.sprite = pygame.sprite.Sprite(self.group) 

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = axis_x
        self.sprite.rect[1] = axis_y

        self.frame = 1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)
    
    def animation(self, image: str, tick: int, frames: int):
        self.tick += 1
        if self.tick == tick:
            self.tick = 0 
            self.frame += 1
        
        if self.frame == frames:
            self.frame = 1
        
        self.sprite.image = pygame.image.load(
            f"assets/{image}{str(self.frame)}.png"
        )
    
    def collision(self, group, name):
        collide = pygame.sprite.spritecollide(self.sprite, group, True)  


class TextElement:
    text_screen: str
    size: int

    def __init__(self, text_screen, size):
        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text_screen, True, (255,255,255))
    
    def drawing(self, window, axis_x, axis_y):
        window.blit(self.render, (axis_x, axis_y))
    
    def update_text(self, text_screen):
        self.render = self.font.render(text_screen, True, (255,255,255))