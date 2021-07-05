from gameObject import GameObject


class Enemy(GameObject):
    def __init__(self, x, y, speed):
        super().__init__(x, y, 50, 50, "assets/enemy.png")

        self.speed = speed

    def move(self, max_width):
        if self.x <= 0:
            self.speed = abs(self.speed)
        elif self.x >= max_width - self.width:
            self.speed = -self.speed

        self.x += self.speed
