from __future__ import annotations

import math
import os
from typing import Callable, Tuple

import pygame
from pygame.constants import (KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP,
                              MOUSEMOTION, MOUSEWHEEL)
from pygame.image import load

from BreakoutBasic.utils import Vector2d


class AbstractSprite:
    active = True

    def __init__(self, name: str, size: Tuple[int, int], image_asset: str, destroy_func: Callable[[AbstractSprite], None] = None) -> None:
        self.name = name
        self.size = size
        self.image = load(os.path.join('assets/sprites', image_asset))
        self.position = (0, 0)
        self.destroy_func = destroy_func

    def handle_event(self, event: pygame.event) -> None:
        pass

    def tick(self) -> None:
        pass

    def handle_collision(self, other) -> None:
        pass

    def destroy(self) -> None:
        if self.destroy_func:
            self.destroy_func(self)

    def contains(self, other) -> bool:
        x, y = self.position
        len_x, len_y = self.size
        ox, oy = other.position
        olen_x, olen_y = other.size

        if x >= ox and x + len_x <= ox + olen_x and \
                y >= oy and y + len_y <= oy + olen_y:
            return True

        return False

    def render(self, surface) -> None:
        # TODO
        pass

    def __str__(self) -> str:
        return f'{self.name} at ({self.position[0]:.2f}, {self.position[1]:.2f}).'


class StaticSprite(AbstractSprite):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class DynamicSprite(AbstractSprite):

    def __init__(self, vector: Vector2d = None, *args, **kwargs) -> None:
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
        return f'{s} Vector :: {self.vector}.'
