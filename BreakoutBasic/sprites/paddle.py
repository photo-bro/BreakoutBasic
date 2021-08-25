import pygame.constants as KEYS

from ..game_globals import WINDOW_SIZE
from ..utils import Rect, Vector2d
from .sprite import DynamicSprite


class Paddle(DynamicSprite):
    _max_speed = 10
    _friction = 0.5
    _pressed = False

    def __init__(self):
        super().__init__(
            vector=Vector2d(0, 3.14),
            **{
                "name": "paddle",
                "rect": Rect(0, 0, 50, 12),
                "image_asset": "paddle_12x50.png",
            }
        )

    def handle_keyboard_event(self, event):
        # print(f'Keyboard event: {event.type}')

        if event.type == KEYS.KEYDOWN:
            if event.key in (KEYS.K_LEFT, KEYS.K_RIGHT):
                self._pressed = True
                if event.key == KEYS.K_LEFT:
                    self.vector.direction = 3.14
                else:
                    self.vector.direction = 0

                # self.vector.mirror_x()
                # self.vector.direction = (-1 if event.key == KEYS.K_LEFT else 1)

        if event.type == KEYS.KEYUP:
            self._pressed = False

    def handle_mouse_event(self, event):
        # print(f'Mouse event: {event}')
        pass

    def move(self):
        window_x, _ = WINDOW_SIZE
        w = self.rect.w
        x, y = self.rect.x, self.rect.y
        mx = self.vector.x

        # print(f'Padde: {self.position} :: {self.direction} :: {self.velocity}')

        if x + w + mx > window_x:
            x = window_x - w
        elif x + mx < 0:
            x = 0
        else:
            x += mx
        self.rect.x = x
        self.rect.y = y

    def tick(self):
        if self._pressed:
            self.vector.magnitude = self._max_speed
        else:
            if self.vector.magnitude > 0:
                self.vector.magnitude -= self._friction
            else:
                self.vector.magnitude = 0
        if self.vector.magnitude != 0:
            self.move()
