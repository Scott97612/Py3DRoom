import pygame as pg
from settings import *

class ObjectRender:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/bg/sky_loop.png', (WIDTH, HALF_HEIGHT))
        #self.ground_image = self.get_texture('resources/bg/aerial_loop.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset, self.ground_offset = 0, 0

    def draw(self):
        self.render_game_objects()

    def draw_sky_floor(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))
        # self.ground_offset = (self.ground_offset + 4.5 * self.game.player.rel) % WIDTH
        # self.screen.blit(self.ground_image, (-self.ground_offset, HALF_HEIGHT))
        # self.screen.blit(self.ground_image, (-self.ground_offset + WIDTH, HALF_HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.jpg'),
            2: self.get_texture('resources/textures/2.jpg'),
            3: self.get_texture('resources/others/TV_hbo_l.png'),
            4: self.get_texture('resources/others/TV_hbo_r.png'),
            5: self.get_texture('resources/others/painting1.jpg'),
            6: self.get_texture('resources/others/painting2.jpg'),
            7: self.get_texture('resources/others/painting3.jpg'),
            8: self.get_texture('resources/others/painting4.jpg'),
            9: self.get_texture('resources/others/painting5.jpg'),
            10: self.get_texture('resources/others/painting6.jpg'),
            11: self.get_texture('resources/others/painting7.jpg'),
            12: self.get_texture('resources/others/painting8.jpg'),
            13: self.get_texture('resources/others/painting9.jpg'),
            14: self.get_texture('resources/others/painting10.jpg'),
            15: self.get_texture('resources/others/door_l.png'),
            16: self.get_texture('resources/others/door_r.png'),
            17: self.get_texture('resources/others/fire.jpg'),
            18: self.get_texture('resources/others/TV_news_l.png'),
            19: self.get_texture('resources/others/TV_news_r.png'),
            20: self.get_texture('resources/others/TV_sport_l.png'),
            21: self.get_texture('resources/others/TV_sport_r.png'),
            22: self.get_texture('resources/others/painting11.jpg'),
            23: self.get_texture('resources/others/painting12.jpg'),
            24: self.get_texture('resources/others/stereos.jpg'),
        }