import pygame as pg


class Tile(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.sprite_tile = pg.image.load("Sprites/block/block.png")
        self.sprite_tile_die = [pg.image.load(f"Sprites/block_die/block_die{0}.png") for i in range(0, 6)]

        self.image = self.sprite_tile
        self.current_sprite = 0
        self.rect = self.sprite_tile.get_rect()
        self.rect.bottomleft = [x, y]

    def update(self, scroll):
        #  оновлюємо положення блоків
        self.rect.x += scroll

    def die(self):
        self.image = self.sprite_tile_die[self.current_sprite]
