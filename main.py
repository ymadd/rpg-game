import pygame

pygame.init()
width = 800
heigh = 800
white_color = (255, 255, 255)

game_window = pygame.display.set_mode((width, heigh))
game_window.fill(white_color)
pygame.display.update()

pygame.quit()
quit()
