import pygame.constants as KEYS

from game_globals import WINDOW_SIZE
from sprites import DynamicSprite


class Paddle(DynamicSprite):
    _max_speed = 10
    _friction = 0.5
    _pressed = False

    def __init__(self):
        super().__init__(**{
            'name': 'paddle',
            'size': (50, 12),
            'image_asset': 'paddle_12x50.png'
        })

    def handle_keyboard_event(self, event):
        # print(f'Keyboard event: {event.type}')

        if event.type == KEYS.KEYDOWN:
            if event.key in (KEYS.K_LEFT, KEYS.K_RIGHT):
                self._pressed = True
                self.direction = (-1 if event.key == KEYS.K_LEFT else 1, 0)

        if event.type == KEYS.KEYUP:
            self._pressed = False

    def handle_mouse_event(self, event):
        # print(f'Mouse event: {event}')
        pass

    def move(self):
        window_x, _ = WINDOW_SIZE
        size_x, _ = self.size
        x, y = self.position
        vel_x, _ = self.velocity

        # print(f'Padde: {self.position} :: {self.direction} :: {self.velocity}')

        if x + size_x + vel_x > window_x:
            x = window_x - size_x
        elif x + vel_x < 0:
            x = 0
        else:
            x += vel_x
        self.position = (x, y)

    def tick(self):
        if self._pressed:
            self.speed = self._max_speed
        else:
            if self.speed > 0:
                self.speed -= self._friction
            else:
                self.speed = 0
        if self.speed != 0:
            self.move()
