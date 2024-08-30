import pygame as pg
import sys
from settings import *
from map import *
from player import *
from ray_casting import *
from object_render import *
from objects_compiler import *

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont(None, 50)
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_render = ObjectRender(self)
        self.raycasting = Ray_Casting(self)
        self.objectscompiler = ObjectsCompile(self)

    def update(self):
        fps = self.font.render(f'FPS: {int(self.clock.get_fps())}', True, (0, 0, 0))
        self.screen.blit(fps, (0, 0))
        self.player.update()
        self.raycasting.update()
        self.objectscompiler.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption('Py3D')



    def draw(self):
        #self.screen.fill('black')
        #self.map.draw()
        #self.player.draw()
        self.object_render.draw_sky_floor()
        self.object_render.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()