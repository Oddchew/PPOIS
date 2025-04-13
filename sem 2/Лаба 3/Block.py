from pygame import Rect, transform
import pygame as pg

from setings import HEIGHT, TEXTURE_PATH, WIDTH
class Block:
    def __init__(self, x, y, texture = None, color = (0,0,0), hits = 1):
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.hits = hits
        self.color = color
        if texture:
            self.texture = transform.scale(texture, (WIDTH, HEIGHT))
            self.texture.fill(color, special_flags=pg.BLEND_MULT)

    
    def hit(self, damage = 1):
        if self.hits > 0:
            self.hits -= damage
        if self.hits > 0:
            block_health =  self.hits-1 if self.hits > 1 else ''
            texture = pg.image.load(f"{TEXTURE_PATH}Block{block_health}.png").convert_alpha()
            self.texture = transform.scale(texture, (WIDTH, HEIGHT))
            self.texture.fill(self.color, special_flags=pg.BLEND_MULT)
        return self.hits == 0