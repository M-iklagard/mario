import pygame as pg
import sys
from player import Player
from tile import Tile
from enemy import Enemy
from bonus import Bonus


# Функція для підрахунуку балів
def scores(surface, player):
    font = pg.font.SysFont("comicsansms", 30)
    label = font.render(f"Scores: {player.scores}",True, [255, 0, 0])
    surface.blit(label, (0, 0))


# налаштування
pg.init()
W = 800
H = 600
background_img = pg.image.load("Sprites/background/background.png")
display = pg.display.set_mode((W, H))
clock = pg.time.Clock()
FPS = 60


move_speed = 5
scroll_line = 400
scroll = 0

# створено групи спрайтів
player_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()
blocks_group = pg.sprite.Group()
bonus_group = pg.sprite.Group()

# створення гравця
player = Player(0, 550)

# Створення списку бонусів
bonus_list = []
bonus_coords = [(450, 150), (1050, 350), (1500, 300), (1750, 450), (1850, 350), (2050, 350), (2150, 450)]
for coord in bonus_coords:
    bonus = Bonus(coord[0], coord[1])
    bonus_list.append(bonus)

# створення списку ворогів
enemy_list = []
enemy_coord_list = [(1200, 250), (550, 550), (1450, 550)]

for coord in enemy_coord_list:
    enemy = Enemy(coord[0], coord[1])
    enemy_list.append(enemy)

# створення списку тайлів
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
              (1900, 600), (1950, 600), (2000, 600), (2250,600), (2300,600),
              (2350,600), (2400,600), (2450,600), (2500,600), (2550,600),
              (2600,600), (2650,600), (2700,600), (2750,600), (2800,600),
              (2850,600), (2900,600), (2950,600), (3000,600), (3050,600),
              (3100,600), (3150,600), (3200,600), (3250,600), (3300,600),
              (3350,600), (2050,600), (2100,600), (2150,600), (2200,600),
              (1950, 350), (1950, 400), (1950, 450), (1950, 500), (1950, 550),
              (900, 600),(1200, 600)]

for coord in coord_list:
    block = Tile(coord[0], coord[1])
    blocks_list.append(block)

# додоємо еземпляри у групи
blocks_group.add(blocks_list)
player_group.add(player)
enemy_group.add(enemy_list)
bonus_group.add(bonus_list)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    display.blit(background_img,(0, 0))

    # межа скролінгу наглядно
    # pg.draw.line(display,(255,0,0),(scroll_line, 0), (scroll_line, H))
    blocks_group.update(scroll)

    # відмальовується група спрайтів
    player_group.draw(display)
    # змінюється положення спрайту
    enemy_group.draw(display)

    blocks_group.draw(display)

    bonus_group.draw(display)

    scroll = player.update(0.1, blocks_group,  enemy_list, bonus_list, W, scroll_line)

    scores(display, player)

    for bonus in bonus_list:
        bonus.update(0.1, scroll)

    for enemy in enemy_list:
        enemy.update(0.1, scroll)
    # print(scroll)

    pg.display.flip()
    clock.tick(FPS)
