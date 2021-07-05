from gameObject import GameObject


class Player(GameObject):
    # definition of the player
    def __init__(self, x, y, speed):
        super().__init__(x, y, 50, 50, "assets/player.png")

        self.speed = speed

    def move(self, direction, max_height):
        if (self.y >= max_height - self.height and direction > 0) or (
                self.y == 0 and direction < 0):
            return
        self.y += (direction * self.speed)
