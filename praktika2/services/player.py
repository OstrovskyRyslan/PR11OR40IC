from weapons.standard_bullet import StandardBullet
from abc import ABC, abstractmethod

class Player:
    def __init__(self, pygame, screen, color, x, y, move_keys):
        self.pygame = pygame
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.move_keys = move_keys
        self.speed = 5
        self.last_shot_time = 0  
        self.shoot_delay = 500   

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def move(self):
        keys = self.pygame.key.get_pressed()
        if keys[self.move_keys["left"]]:
            self.move_left()
        if keys[self.move_keys["right"]]:
            self.move_right()
        if keys[self.move_keys["up"]]:
            self.move_up()
        if keys[self.move_keys["down"]]:
            self.move_down()
        if keys[self.pygame.K_SPACE]:
            self.attack()

    def draw_player(self):
        self.pygame.draw.rect(self.screen, self.color, (self.x, self.y, 50, 50))

    @abstractmethod
    def attack(self):
        current_time = self.pygame.time.get_ticks()
        if current_time - self.last_shot_time > self.shoot_delay:
            StandardBullet(self.pygame, self.screen, self.x + 25, self.y, 'up')
            self.last_shot_time = current_time  
