import pygame.constants as KEYS

from game_globals import WINDOW_SIZE
from sprites import DynamicSprite


class Paddle(DynamicSprite):
    _max_speed = 25
    _friction = 0

    def __init__(self):
        super().__init__(**{
            'name': 'paddle',
            'size': (50, 12),
            'image_asset': 'paddle_12x50.png'
        })

    def handle_keyboard_event(self, event):
        # print(f'Keyboard event: {event}')

        if event.type == KEYS.KEYDOWN:
            if event.key in (KEYS.K_LEFT, KEYS.K_RIGHT):
                self._friction = 0
                if self.speed < self._max_speed:
                    self.speed += 15
                else:
                    self.speed = self._max_speed
                self.direction = (-1 if event.key == KEYS.K_LEFT else 1, 0)

        if event.type == KEYS.KEYUP:
            self._friction = 1
            if self.speed > 15:
                self.speed -= 15

    def handle_mouse_event(self, event):
        # print(f'Mouse event: {event}')
        pass

    def move(self):
        window_x, _ = WINDOW_SIZE
        size_x, _ = self.size
        x, y = self.position
        vel_x, _ = self.velocity

        if x + size_x + vel_x > window_x:
            x = window_x - size_x
        elif x + vel_x < 0:
            x = 0
        else:
            x += vel_x
        self.position = (x, y)

    def tick(self):
        if self.speed > 0:
            if self.speed < 1:
                self.speed = 0
            else:
                self.speed -= self._friction
        if self.speed != 0:
            self.move()
