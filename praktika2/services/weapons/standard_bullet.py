import pygame
from weapons.base_bullet import BaseBullet

class StandardBullet(BaseBullet):
    def __init__(self, screen, x, y, direction):
        super().__init__(screen, x, y, direction)

    def draw(self):
        self.move()
        pygame.draw.circle(self.screen, (255, 255, 0), (int(self.x), int(self.y)), 5)
