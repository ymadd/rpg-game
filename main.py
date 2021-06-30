import pygame

pygame.init()
width = 800
heigh = 800
white_color = (255, 255, 255)

game_window = pygame.display.set_mode((width, heigh))

clock = pygame.time.Clock()

while True:
    # Handle events
    # Excute logic
    # Update display
    game_window.fill(white_color)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
