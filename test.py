import pygame as pg
import sys
from player import Player
from tile import Tile

pg.init()
W = 2300
H = 600
background_img = pg.image.load("Sprites/background/background.png")
display = pg.display.set_mode((W, H))
clock = pg.time.Clock()
FPS = 60

# створено групу спрайтів гравця
move = pg.sprite.Group()
# створено гравця
player = Player(0, 540)
# до групи спрайтів додано спрайти гравця
move.add(player)

# створено групу спрайтів блоків
blocks = pg.sprite.Group()

blocks_list = []
coord_list = [(450, 200), (350, 250), (1150, 300), (1200, 300), (1250, 300),
              (1300, 300), (1900, 350), (2000, 350), (200, 400), (250, 400),
              (300, 400), (1050, 400), (1100, 400), (1400, 400), (1600, 400),
              (1650, 400), (1850, 400), (1900, 400), (2000, 400), (2050, 400),
              (1800, 450), (1850, 450), (1900, 450), (2000, 450), (2050, 450),
              (2100, 450), (1750, 500), (1800, 500), (1850, 500), (1900, 500),
              (2000, 500), (2050, 500), (2100, 500), (2150, 500), (1700, 550),
              (1750, 550), (1800, 550), (1850, 550), (1900, 550), (2000, 550),
              (2050, 550), (2100, 550), (2150, 550), (2200, 550), (0, 600),
              (50, 600), (100, 600), (150, 600), (200, 600), (250, 600),
              (300, 600), (350, 600), (400, 600), (450, 600), (500, 600),
              (550, 600), (600, 600), (650, 600), (700, 600), (750, 600),
              (800, 600), (850, 600), (950, 600), (1000, 600), (1050, 600),
              (1100, 600), (1150, 600), (1250, 600), (1300, 600), (1350, 600),
              (1400, 600), (1450, 600), (1500, 600), (1550, 600), (1600, 600),
              (1650, 600), (1700, 600), (1750, 600), (1800, 600), (1850, 600),
              (1900, 600), (1950, 600), (2000, 600), (2050, 600), (2100, 600),
              (2150, 600), (2200, 600), (2250, 600), (2300, 600)]

for coord in coord_list:
    block = Tile(coord[0], coord[1])
    blocks_list.append(block)
blocks.add(blocks_list)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    display.blit(background_img, [0, 0])
    # відмальовується група спрайтів
    move.draw(display)
    # змінюється положення спрайту

    blocks.draw(display)
    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        player.is_moving_right = True
        player.is_static = False
        player.is_moving_left = False

        move.update(0.1)
        player.rect.x += 5

    elif keys[pg.K_LEFT]:
        player.is_moving_left = True
        player.is_static = False
        player.is_moving_right = False

        move.update(0.1)
        player.rect.x -= 5

    else:
        player.is_moving_right = False
        player.is_moving_left = False
        player.is_static = True
        move.update(0)

    if keys[pg.K_SPACE] and player.is_jump == False and player.is_fall == False:
        player.is_jump = True
        player.is_static = False
        print(player.is_jump)

    if player.is_jump:
        move.update(0)
        player.jump()

    player.gravity(550)

    if pg.sprite.spritecollideany(player, blocks):

        for sprite in blocks_list:
            # перевіряємо нижню сторону
            if player.rect.bottom - sprite.rect.top in range(0, 30):
                player.rect.y += 11
            # перевіряємо верхню сторону
            if player.rect.top - sprite.rect.bottom in range(-30, 0):
                player.rect.y -= 11
            # перевіряємо ліву сторону
            if player.rect.left - sprite.rect.right in range(-30, 0):
                player.rect.x -= 11
            # перевіряємо праву сторону
            if player.rect.right - sprite.rect.left in range(0, 30):
                player.rect.x += 11

    print(player.rect.bottomleft)

    pg.display.flip()
    clock.tick(FPS)
