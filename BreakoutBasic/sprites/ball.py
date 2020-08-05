import math
import random

import pygame

from BreakoutBasic.game_globals import WINDOW_SIZE
from BreakoutBasic.utils import Vector2d

from .brick import Brick
from .sprite import AbstractSprite, DynamicSprite


class Ball(DynamicSprite):

    def __init__(self) -> None:
        super().__init__(**{
            'vector': Vector2d(5, random.uniform(0, 2*math.pi)),
            'name': 'ball',
            'size': (5, 5),
            'image_asset': 'ball_5x5.png'
        })

    def handle_keyboard_event(self, event: pygame.event) -> None:
        pass

    def handle_mouse_event(self, event: pygame.event) -> None:
        pass

    def handle_collision(self, other: AbstractSprite) -> None:
        self.bounce(other)

        if isinstance(other, Brick):
            other.destroy()

        # if isinstance(other, sprites.Paddle):
        #     pass

    def bounce(self, other: AbstractSprite) -> None:
        # Assumes there is a collision already
        # print(f'pos {self.position} other.pos: {other.position}. other size: {other.size}')
        x, y = self.position
        sx, sy = self.size
        ox, oy = other.position
        osx, osy = other.size

        if y >= oy and y + sy <= oy + osy:  # inside vertically
            print('inside vert')
            self.vector.mirror_x()
        if x >= ox and x + sx <= ox + osx:  # inside horizontally
            # if ox <= x <= ox +osx:
            print('inside horz')
            self.vector.mirror_y()

        # Add a little randomness
        self.vector.direction += random.uniform(-0.1, 0.1)

    def move(self) -> None:
        # print(str(self))
        window_x, window_y = WINDOW_SIZE
        size_x, size_y = self.size
        x, y = self.position

        sx, sy = self.vector.x, self.vector.y

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
            # y = 0
            self.vector.mirror_y()

        self.position = (x + sx, y+sy)

    def tick(self) -> None:
        self.move()
