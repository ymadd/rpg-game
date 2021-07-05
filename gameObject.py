import pygame


class GameObject:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, (self.width, self.height))
