from __future__ import annotations

import os
from typing import Callable, List, Optional

from pygame.constants import (KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP,
                              MOUSEMOTION, MOUSEWHEEL)
from pygame.event import Event
from pygame.image import load
from pygame.surface import Surface

from ..utils import FloatPoint, Rect, Vector2d


class AbstractSprite:
    active: bool = True
    name: str
    rect: Rect
    image: Surface
    destroy_func: Optional[Callable[[AbstractSprite], None]]

    def __init__(
        self,
        name: str,
        rect: Rect,
        image_asset: str,
        destroy_func: Optional[Callable[[AbstractSprite], None]] = None,
    ) -> None:
        self.name = name
        self.rect = rect
        self.image = load(os.path.join("assets/sprites", image_asset))
        self.destroy_func = destroy_func

    def handle_event(self, event: Event) -> None:
        pass

    def tick(self, colliding_sprites: List[AbstractSprite]) -> None:
        pass

    def destroy(self) -> None:
        if self.destroy_func:
            self.destroy_func(self)

    def contains(self, other: AbstractSprite) -> bool:
        return self.rect.intersects(other.rect)

    def render(self, surface: Surface) -> None:
        # TODO
        pass

    def __str__(self) -> str:
        return f"{self.name} at ({self.rect.x:.2f}, {self.rect.y:.2f})."


class StaticSprite(AbstractSprite):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class DynamicSprite(AbstractSprite):
    velocity: FloatPoint = FloatPoint(0.0, 0.0)

    def __init__(
        self,
        *args,
        velocity: Optional[FloatPoint] = None,
        **kwargs,
    ) -> None:
        if velocity:
            self.velocity = velocity
        super().__init__(*args, **kwargs)


class DynamicVectorSprite(AbstractSprite):
    def __init__(self, *args, vector: Vector2d = None, **kwargs) -> None:
        if vector:
            self.vector = vector
        else:
            self.vector = Vector2d(1, 0)

        super().__init__(*args, **kwargs)

    def handle_event(self, event: Event) -> None:
        if event.type in (KEYDOWN, KEYUP):
            self.handle_keyboard_event(event)
        elif event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEWHEEL):
            self.handle_mouse_event(event)

    def handle_keyboard_event(self, event: Event) -> None:
        raise NotImplementedError()

    def handle_mouse_event(self, event: Event) -> None:
        raise NotImplementedError()

    def __str__(self) -> str:
        s = super().__str__()
        return f"{s} Vector :: {self.vector}."
