import sys
import os
import pygame

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from players.player_green import PlayerGreen
from players.player_red import PlayerRed
from renderer import Renderer

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Два плеера")

background = pygame.image.load(r'C:\Users\Ruslan Ostrovsky\Desktop\praktika\services\fon\fon.png')
background = pygame.transform.scale(background, (800, 600))

green_player = PlayerGreen(100, 100, screen)
red_player = PlayerRed(200, 200, screen)

background_x = 0
background_speed = 2
screen_width = screen.get_width()
screen_height = screen.get_height()

clock = pygame.time.Clock()
running = True

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                green_player.shoot()
            if event.key == pygame.K_RETURN:  
                red_player.shoot()


    green_player.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    red_player.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    for player in [green_player, red_player]:
        if player.x < 0:
            player.x = 0
        elif player.x + 50 > screen_width:
            player.x = screen_width - 50
        if player.y < 0:
            player.y = 0
        elif player.y + 50 > screen_height:
            player.y = screen_height - 50

 
    if green_player.x > screen_width - 100 or red_player.x > screen_width - 100:
        background_x -= background_speed
    if green_player.x < 100 or red_player.x < 100:
        background_x += background_speed


    if background_x <= -screen_width:
        background_x = 0
    elif background_x >= 0:
        background_x = -screen_width


    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + screen_width, 0))

 
    Renderer.render_all()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
