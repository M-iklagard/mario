import sys

import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # завантажуємо зображення
        self.sprite_front = pg.image.load("Sprites/mario_static/marioF.png")
        self.sprite_jump = pg.image.load("Sprites/mario_jump/mario_jump.png")
        self.sprites_right = [pg.image.load(f"Sprites/mario_right/mario{i}.png") for i in range(0, 4)]
        self.sprites_left = [pg.image.load(f"Sprites/mario_left/mario{i}.png") for i in range(0, 4)]

        # поточний номер спрайту
        self.current_sprite = 0
        # поточний спрайт
        self.image = self.sprite_front
        # прямокутна область поточного спрайту
        self.rect = self.image.get_rect()
        # координати для розміщення
        self.rect.bottomleft = [x, y]
        # Прискорення при стрибку
        self.vel_y = 0
        self.scores = 0

        # стани
        self.is_jump = False
        self.is_in_air = False
        self.walked_way_right = 0

    def update(self, speed: float, tile_list: list, enemy_list: list, bounus_list, window_width, scroll_line):
        dx = 0
        dy = 0
        scroll = 0
        key = pg.key.get_pressed()

        if not self.is_in_air:
            self.image = self.sprite_front

        if key[pg.K_RIGHT]:
            if self.current_sprite >= len(self.sprites_right):
                self.current_sprite = 0
            self.image = self.sprites_right[int(self.current_sprite)]

            dx += 5

        if key[pg.K_LEFT]:
            if self.current_sprite >= len(self.sprites_left):
                self.current_sprite = 0
            self.image = self.sprites_left[int(self.current_sprite)]

            dx -= 5

        if key[pg.K_SPACE] and self.is_jump is False and not self.is_in_air:
            self.image = self.sprite_jump
            self.vel_y -= 35
            self.is_jump = True

        if key[pg.K_SPACE] is False:
            self.is_jump = False

        #  Гравітація
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # check for collision
        self.is_in_air = True

        #  Колізії з рамками екрана
        if self.rect.left == 0:
            dx += 5
        elif self.rect.right == window_width:
            dx -= 5

        for tile in tile_list:
            #  Колізії по x
            if tile.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            #  Колізії по y
            if tile.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):

                if self.vel_y < 0:
                    dy = tile.rect.bottom - self.rect.top
                    self.vel_y = 0
                    # tile.die()
                    tile.kill()
                elif self.vel_y >= 0:
                    dy = tile.rect.top - self.rect.bottom
                    self.is_in_air = False

        # Перевіряє чи досягнув персонаж межу прокрутки
        if self.walked_way_right < 2600:
            if self.rect.right > scroll_line:
                if dx > 0:
                    scroll = - dx
                    self.walked_way_right += dx

        self.current_sprite += speed
        self.rect.x += dx+scroll
        self.rect.y += dy

        # перевірка на вбивство)
        for enemy in enemy_list:
            if self.is_in_air:
                if enemy.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    enemy.die()
            else:
                if enemy.is_alive:
                    if enemy.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                        sys.exit()

        for bonus in bounus_list:
            if bonus.rect.colliderect(self.rect):
                if bonus.is_active:
                    self.scores += 1
                    bonus.kill()
                    bonus.is_active = False

        return scroll



