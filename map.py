import pygame as pg
from map_design import *

class Map:
    def __init__(self, game):
        self.game = game
        self.map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.map):  # every row of self.map
            for i, value in enumerate(row):  # every column of self.map
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2) for pos in self.world_map]