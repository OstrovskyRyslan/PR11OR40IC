import pygame
from weapons.standard_bullet import StandardBullet
from renderer import Renderer
from abc import ABC, abstractmethod

class PlayerRed:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.speed = 5
        self.bullets = []

        Renderer.add_object(self)

    def move(self, keys, up, down, left, right):
        if keys[up]:
            self.y -= self.speed
        if keys[down]:
            self.y += self.speed
        if keys[left]:
            self.x -= self.speed
        if keys[right]:
            self.x += self.speed

    def shoot(self):
        bullet = StandardBullet(self.screen, self.x + 25, self.y, 'up')
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, 50, 50))
