import pygame
from screen_elements import ScreenElements

class MenuScene:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.backgroud_image = ScreenElements("assets/sky.png", 0, 0, self.all_sprites)
        self.backgroud_image_aux = ScreenElements("assets/sky.png", 360, 0, self.all_sprites)
        self.ground = ScreenElements("assets/ground.png", 0, 480, self.all_sprites)
        self.ground_aux = ScreenElements("assets/ground.png", 360, 480, self.all_sprites)

        self.logo = ScreenElements("assets/getready.png", 55, 100, self.all_sprites)
        self.score_table = ScreenElements("assets/score.png", 20, 200, self.all_sprites)
        self.button_go = ScreenElements("assets/go.png", 100, 420, self.all_sprites)

        self.change_scene = False

    def draw(self, window):
        self.all_sprites.draw(window)
    
    def update(self):
        self.all_sprites.update()
        self.move_bg()
        self.move_groud()

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_go.rect.collidepoint(pygame.mouse.get_pos()):
                self.change_scene = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.change_scene = True

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


class GameOverScene(MenuScene):
    def __init__(self, image):
        super().__init__(image)
    
    