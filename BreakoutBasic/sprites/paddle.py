import pygame.constants as KEYS

from game_globals import WINDOW_SIZE
from sprites import AbstractSprite


class Paddle(AbstractSprite):
    _button_pressed = False
    _move_delta = 0

    def __init__(self):
        super().__init__(**{
            'name': 'paddle',
            'size': (50, 12),
            'image_asset': 'paddle_12x50.png'
        })

    def handle_keyboard_event(self, event):
        # print(f'Keyboard event: {event}')

        if event.type == KEYS.KEYDOWN:
            self._button_pressed = True
            if event.key in (KEYS.K_LEFT, KEYS.K_RIGHT):
                self._move_delta = (
                    25 * (-1 if event.key == KEYS.K_LEFT else 1))

        if event.type == KEYS.KEYUP:
            self._button_pressed = False
            self._move_delta = 0

    def handle_mouse_event(self, event):
        # print(f'Mouse event: {event}')
        pass

    def move_horizontal(self):
        window_x, _ = WINDOW_SIZE
        size_x, _ = self.size
        x, y = self.position
        if x + size_x + self._move_delta > window_x:
            x = window_x - size_x
        elif x + self._move_delta < 0:
            x = 0
        else:
            x += self._move_delta
        self.position = (x, y)

    def tick(self):
        if self._move_delta != 0:
            self.move_horizontal()
