import math
import random

import pygame

import sprites
from game_globals import WINDOW_SIZE
from utils import Vector2d


class Ball(sprites.DynamicSprite):

    def __init__(self):
        super().__init__(**{
            'speed': 5,
            'vector': Vector2d(1, random.uniform(0, 2*math.pi)),
            'name': 'ball',
            'size': (5, 5),
            'image_asset': 'ball_5x5.png'
        })

    def handle_keyboard_event(self, event: pygame.event):
        pass

    def handle_mouse_event(self, event: pygame.event):
        pass

    def handle_collision(self, other: sprites.AbstractSprite):
        if isinstance(other, sprites.Brick):
            other.destroy()

        if isinstance(other, sprites.Paddle):
            pass
        # self.bounce(other)

    def bounce(self, other: sprites.AbstractSprite):
        dx, dy = self.direction
        x, y = self.position
        ox, oy = other.position
        sx, sy = other.size

        if oy == y <= oy + sy:  # inside vertically
            dy = -dy
        if ox == x <= ox + sx:  # inside horizontally
            dx = -dx

        self.direction = (dx, dy)

    def move(self):
        # print(str(self))
        window_x, window_y = WINDOW_SIZE
        size_x, size_y = self.size
        x, y = self.position

        sx, sy = (self.speed * self.vector.x, self.speed * self.vector.y)

        if x + size_x + sx > window_x:  # right wall
            x = window_x - size_x
            self.vector.mirror_x()

        if y + size_y + sy > window_y:  # bottom wall
            y = window_y - size_y
            self.vector.mirror_y()

        if x + sx < 0:  # left wall
            # x = 0
            self.vector.mirror_x()

        if y + sy < 0:  # top wall
            y = 0
            self.vector.mirror_y()

        self.position = (x + sx, y+sy)

    def tick(self):
        self.move()
