import pygame


class Game:
    def __init__(self):
        self.width = 800
        self.heigh = 800
        self.white_color = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.heigh))

        background_image = pygame.image.load("assets/background.png")
        self.background_image = pygame.transform.scale(
                background_image, (self.width, self.heigh))

        tresure_image = pygame.image.load("assets/treasure.png")
        self.tresure_image = pygame.transform.scale(tresure_image, (50, 50))

        self.clock = pygame.time.Clock()

    def draw_object(self):
        self.game_window.fill(self.white_color)

        self.game_window.blit(self.background_image, (0, 0))
        self.game_window.blit(self.tresure_image, (375, 50))

        pygame.display.update()

    def run_game_loop(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return

            self.draw_object()

            self.clock.tick(60)
