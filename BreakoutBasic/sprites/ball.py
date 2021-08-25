import math
import random

from pygame.event import Event

from ..game_globals import WINDOW_SIZE
from ..utils import Rect, Vector2d
from .brick import Brick
from .sprite import AbstractSprite, DynamicSprite


class Ball(DynamicSprite):
    def __init__(self) -> None:
        super().__init__(
            vector=Vector2d(2, random.uniform(0, 2 * math.pi)),
            **{"name": "ball", "rect": Rect(0, 0, 5, 5), "image_asset": "ball_5x5.png"},
        )

    def handle_keyboard_event(self, event: Event) -> None:
        pass

    def handle_mouse_event(self, event: Event) -> None:
        pass

    def handle_collision(self, other: AbstractSprite) -> None:
        self.bounce(other)

        if isinstance(other, Brick):
            other.destroy()

        # if isinstance(other, sprites.Paddle):
        #     pass

    def bounce(self, other: AbstractSprite) -> None:
        # Assumes there is a collision already
        print(f"Bounce! {self} and {other}")
        x, y = self.rect.x, self.rect.y
        w, h = self.rect.w, self.rect.h
        ox, oy = other.rect.x, other.rect.y
        ow, oh = other.rect.w, other.rect.h

        if y >= oy and y + h <= oy + oh:  # inside vertically
            print("inside vert")
            self.vector.mirror_x()
        if x >= ox and x + w <= ox + ow:  # inside horizontally
            print("inside horz")
            self.vector.mirror_y()

        # Add a little randomness
        self.vector.direction += random.uniform(-0.1, 0.1)

    def move(self) -> None:
        # print(str(self))
        window_x, window_y = WINDOW_SIZE
        w, h = self.rect.w, self.rect.h
        x, y = self.rect.x, self.rect.y

        mx, my = self.vector.x, self.vector.y

        if x + w + mx > window_x:  # right wall
            x = window_x - w
            self.vector.mirror_x()

        if y + h + my > window_y:  # bottom wall
            y = window_y - h
            self.vector.mirror_y()

        if x + mx < 0:  # left wall
            x += int(-mx)
            self.vector.mirror_x()

        if y + my < 0:  # top wall
            y += int(-my)
            self.vector.mirror_y()

        self.rect.x = int(x + mx)
        self.rect.y = int(y + my)

    def tick(self) -> None:
        self.move()
