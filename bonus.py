import pygame as pg


class Bonus(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.bonus_sprite = [pg.image.load(f"Sprites/coin/coin{i}.png") for i in range(0, 4)]

        self.current_sprite = 0
        self.image = self.bonus_sprite[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [x, y]
        self.is_active = True

    def update(self, speed, scroll):
        if self.current_sprite >= len(self.bonus_sprite):
            self.current_sprite = 0
        self.image = self.bonus_sprite[int(self.current_sprite)]

        self.current_sprite += speed
        self.rect.x += scroll


