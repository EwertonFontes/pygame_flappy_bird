import pygame
from menu import MenuScene, GameOverScene
from game import GameScene

class MainScreen:
    def __init__(self, sizex, sizey, title):
        pygame.init()
        
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)
        self.loop = True
        self.fps = pygame.time.Clock()

        self.game = GameScene()
       
    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False


    def draw(self):
        self.game.draw(self.window)
        self.game.update()


    def update(self):
       while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.update()