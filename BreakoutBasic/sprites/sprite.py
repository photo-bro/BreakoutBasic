from __future__ import annotations

import math
import os
from typing import Callable, Optional, Tuple

import pygame
from pygame.constants import (KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP,
                              MOUSEMOTION, MOUSEWHEEL)
from pygame.image import load

from BreakoutBasic.utils import Vector2d, Rect


class AbstractSprite:
    active: bool = True
    name: str
    rect: Rect
    image: pygame.image
    destroy_func: Optional[Callable[[AbstractSprite], None]]

    def __init__(self, name: str, rect: Rect, image_asset: str,
                 destroy_func: Optional[Callable[[AbstractSprite], None]] = None) -> None:
        self.name = name
        self.rect = rect
        self.image = load(os.path.join('assets/sprites', image_asset))
        self.destroy_func = destroy_func

    def handle_event(self, event: pygame.event) -> None:
        pass

    def tick(self) -> None:
        pass

    def handle_collision(self, other: AbstractSprite) -> None:
        pass

    def destroy(self) -> None:
        if self.destroy_func:
            self.destroy_func(self)

    def contains(self, other: AbstractSprite) -> bool:
        return self.rect.contains(other.rect)

    def render(self, surface: pygame.Surface) -> None:
        # TODO
        pass

    def __str__(self) -> str:
        return f'{self.name} at ({self.rect.x}, {self.rect.y}).'


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

    def handle_event(self, event: pygame.event) -> None:
        if event.type in (KEYDOWN, KEYUP):
            self.handle_keyboard_event(event)
        elif event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEWHEEL):
            self.handle_mouse_event(event)

    def handle_keyboard_event(self, event: pygame.event) -> None:
        raise NotImplementedError()

    def handle_mouse_event(self, event: pygame.event) -> None:
        raise NotImplementedError()

    def __str__(self) -> str:
        s = super().__str__()
        return f'{s} Vector :: {self.vector}.'
