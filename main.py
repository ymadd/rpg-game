import pygame

pygame.init()
width = 800
heigh = 800
white_color = (255, 255, 255)

game_window = pygame.display.set_mode((width, heigh))

clock = pygame.time.Clock()

background_image = pygame.image.load("assets/background.png")
background_image = pygame.transform.scale(background_image, (width, heigh))

tresure_image = pygame.image.load("assets/treasure.png")
tresure_image = pygame.transform.scale(tresure_image, (50, 50))


def run_game_loop():
    while True:
        # Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        # Excute game logic
        # Update display
        game_window.fill(white_color)
        game_window.blit(background_image, (0, 0))
        game_window.blit(tresure_image, (375, 50))
        pygame.display.update()

        clock.tick(60)


run_game_loop()
pygame.quit()
quit()
