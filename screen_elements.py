
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
    
    def animation(self, image: str, tick: int, frames: int):
        self.tick += 1
        if self.tick == tick:
            self.tick = 0 
            self.frame += 1
        
        if self.frame == frames:
            self.frame = 1
        
        self.image = pygame.image.load(
            f"assets/{image}{str(self.frame)}.png"
        )
    
    def collision(self, group, name):
        collide = pygame.sprite.spritecollide(self.sprite, group, True)  


class TextElements:
    text_screen: str
    size: int

    def __init__(self, text_screen, size):
        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text_screen, True, (255,255,255))
    
    def drawing(self, window, axis_x, axis_y):
        window.blit(self.render, (axis_x, axis_y))
    
    def update_text(self, text_screen):
        self.render = self.font.render(text_screen, True, (255,255,255))