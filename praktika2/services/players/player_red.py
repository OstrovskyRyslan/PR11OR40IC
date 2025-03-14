import pygame
from renderer import Renderer
from interfaces.drowable import Drawable

class PlayerRed(Drawable):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.width = 50
        self.height = 50
        self.color = (255, 0, 0)  
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

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def shoot(self):
        from weapons.standard_bullet import StandardBullet  
        bullet = StandardBullet(self.screen, self.x + 25, self.y, 'down')
        self.bullets.append(bullet)

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.move()
            bullet.draw()
