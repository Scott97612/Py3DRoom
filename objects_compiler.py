from sprites import *

class ObjectsCompile:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.get_sprites()

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def update(self):
        for sprite in self.sprite_list:
            sprite.update()

    def get_sprites(self):
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (10.2, 11.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (11.82, 11.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (10.2, 13.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (11.82, 13.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (10.2, 15.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (11.82, 15.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (10.2, 17.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (11.82, 17.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (10.2, 19.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (11.82, 19.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (7.5, 3)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (14.5, 3)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (7.5, 4)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (14.5, 4)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (7.5, 5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (14.5, 5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (7.5, 7.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (14.5, 7.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (10, 2.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp2.png', (12, 2.5)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (9.5, 10.8)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (12.5, 10.8)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (7.5, 10.8)))
        self.add_sprite(Sprites(self.game, 'resources/sprites/lamp1.png', (14.5, 10.8)))
        self.add_sprite(Animate(self.game, 'resources/sprites/green_light/0.png', (10.1, 3.5), scale=0.7, shift=0.27))
        self.add_sprite(Animate(self.game, 'resources/sprites/red_light/0.png', (11.9, 3.5), scale=0.7, shift=0.27))
        self.add_sprite(Animate(self.game, 'resources/sprites/green_light/0.png', (10.4, 20.8), scale=0.7, shift=0.27))
        self.add_sprite(Animate(self.game, 'resources/sprites/red_light/0.png', (11.6, 20.8), scale=0.7, shift=0.27))
        self.add_sprite(Animate(self.game, 'resources/sprites/green_light/0.png', (20.6, 8.4), scale=0.7, shift=0.27))
        self.add_sprite(Animate(self.game, 'resources/sprites/red_light/0.png', (20.6, 9.6), scale=0.7, shift=0.27))
        self.add_sprite(Animate(self.game, 'resources/sprites/green_light/0.png', (1.4, 8.4), scale=0.7, shift=0.27))
        self.add_sprite(Animate(self.game, 'resources/sprites/red_light/0.png', (1.4, 9.6), scale=0.7, shift=0.27))