import math
import os
from typing import Callable, Tuple

import pygame
from pygame.constants import (KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP,
                              MOUSEMOTION, MOUSEWHEEL)
from pygame.image import load
from utils import Vector2d


class AbstractSprite:
    active = True

    def __init__(self, name: str, size: Tuple[int, int], image_asset: str, destroy_func: Callable = None):
        self.name = name
        self.size = size
        self.image = load(os.path.join('assets/sprites', image_asset))
        self.position = (0, 0)
        self.destroy_func = destroy_func

    def handle_event(self, event: pygame.event):
        pass

    def tick(self):
        pass

    def handle_collision(self, other):
        pass

    def destroy(self):
        if self.destroy_func:
            self.destroy_func(self)

    def contains(self, other):
        x, y = self.position
        len_x, len_y = self.size
        ox, oy = other.position
        olen_x, olen_y = other.size

        if ox >= x and ox + olen_x <= x + len_x:
            pass
        else:
            return False

        if oy >= y and oy + olen_y <= y + len_y:
            return True

        return False

    def __str__(self):
        return f'{self.name} at ({self.position[0]:.2f}, {self.position[1]:.2f}).'


class StaticSprite(AbstractSprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DynamicSprite(AbstractSprite):

    def __init__(self, speed: float = 0, vector: Vector2d = None, * args, **kwargs):
        self.speed = speed
        if vector:
            self.vector = vector
        else:
            self.vector = Vector2d(1, 0)

        super().__init__(*args, **kwargs)

    def handle_event(self, event: pygame.event):
        if event.type in (KEYDOWN, KEYUP):
            self.handle_keyboard_event(event)
        elif event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEWHEEL):
            self.handle_mouse_event(event)

    def handle_keyboard_event(self, event: pygame.event):
        raise NotImplementedError()

    def handle_mouse_event(self, event: pygame.event):
        raise NotImplementedError()

    def __str__(self):
        s = super().__str__()
        return f'{s} Speed: {self.speed:.2f} :: Vector :: {self.vector}.'
