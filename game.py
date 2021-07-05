import pygame
from gameObject import GameObject


class Game:
    def __init__(self):
        self.width = 800
        self.heigh = 800
        self.white_color = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.heigh))

        self.background = GameObject(
            0, 0, self.width, self.heigh, 'assets/background.png')
        self.tresure = GameObject(375, 50, 50, 50, 'assets/treasure.png')

        self.clock = pygame.time.Clock()

    def draw_object(self):
        self.game_window.fill(self.white_color)

        self.game_window.blit(
            self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(
            self.tresure.image, (self.tresure.x, self.tresure.y))
        pygame.display.update()

    def run_game_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return

            self.draw_object()

            self.clock.tick(60)
