import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy


class Game:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.white_color = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.background = GameObject(
            0, 0, self.width, self.height, 'assets/background.png')
        self.tresure = GameObject(375, 50, 50, 50, 'assets/treasure.png')

        self.level = 1.0

        self.reset_map()

    def draw_objects(self):
        self.game_window.fill(self.white_color)

        self.game_window.blit(
            self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(
            self.tresure.image, (self.tresure.x, self.tresure.y))
        self.game_window.blit(
            self.player.image, (self.player.x, self.player.y))

        for enemy in self.enemies:
            self.game_window.blit(
                enemy.image, (enemy.x, enemy.y))
        pygame.display.update()

    def detect_collision(self, object1, object2):
        if object1.y > (object2.y + object2.height):
            return False
        elif object1.y + object1.height < object2.y:
            return False

        if object1.x > (object2.x + object2.width):
            return False
        elif object1.x + object1.width < object2.x:
            return False

        return True

    def check_if_colided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level = 1.0
                return True
            if self.detect_collision(self.player, self.tresure):
                self.level += 0.5
                return True
        return False

    def move_object(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)

    def reset_map(self):
        self.player = Player(375, 700, 10)

        speed = 5 + (self.level * 5)

        if self.level >= 4.0:
            self.enemies = [
                Enemy(0, 600, speed),
                Enemy(750, 400, speed),
                Enemy(0, 200, speed),
            ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, 600, speed),
                Enemy(750, 400, speed),
            ]
        else:
            self.enemies = [
                Enemy(0, 600, speed),
            ]

    def run_game_loop(self):
        player_direction = 0
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

            self.move_object(player_direction)

            self.draw_objects()

            # if self.detect_collision(self.player, self.enemy):
            #     return
            # elif self.detect_collision(self.player, self.tresure):
            #     return

            if self.check_if_colided():
                self.reset_map()

            self.clock.tick(60)
