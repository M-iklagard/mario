import pygame as pg
import random


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.enemy_sprite_walk = [pg.image.load(f"Sprites/enemy/gumba{i}.png") for i in range(0, 3)]
        self.enemy_sprite_die = pg.image.load("Sprites/enemy/gumbaDead.png")

        self.current_sprite = 0
        self.image = self.enemy_sprite_walk[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [x, y]

        self.is_alive = True
        self.walked = 0
        self.direction = random.choice(["right", "left"])
        self.death_frame = 0

    def update(self, speed, scroll):
        dx = 0
        if self.is_alive:
            if self.current_sprite >= len(self.enemy_sprite_walk):
                self.current_sprite = 0
            self.image = self.enemy_sprite_walk[int(self.current_sprite)]

            if self.direction == "right":
                dx += random.choice(range(1, 5))
                if self.walked >= 80:
                    self.direction = "left"

            if self.direction == "left":
                dx -= random.choice(range(1, 5))
                if self.walked <= -80:
                    self.direction = "right"

        self.walked += dx

        self.current_sprite += speed
        self.rect.x += dx+scroll

    def die(self):
        self.is_alive = False
        self.image = self.enemy_sprite_die




