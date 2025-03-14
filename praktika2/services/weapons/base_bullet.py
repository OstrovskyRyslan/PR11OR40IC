import pygame
from renderer import Renderer

class BaseBullet:
    def __init__(self, screen, x, y, direction):
        self.screen = screen
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 10
        Renderer.add_object(self)

    def move(self):
        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed

    def draw(self):
        self.move()
        pygame.draw.circle(self.screen, (255, 255, 0), (int(self.x), int(self.y)), 5)
