import json
import pygame as pg
from Block import Block
from setings import TEXTURE_PATH

def load_levels(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data["levels"]

def create_blocks(level_data):
    blocks = []
    for block in level_data["blocks"]:
        texture_name = block["texture"]
        texture = pg.image.load(f"{TEXTURE_PATH}{texture_name}").convert_alpha()
        blocks.append(Block(block["x"], block["y"], texture, color=tuple(block["color"]), hits=block["hits"]))
    return blocks

levels = load_levels("levels.json")