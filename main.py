from main_screen import MainScreen

running = True
while running:
    game = MainScreen(360, 640, "FlappyBird")
    running = game.update()
