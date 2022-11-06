from typing import List

from pygame.event import Event

from ..utils import IntPoint, Rect
from .sprite import AbstractSprite, StaticSprite


class Brick(StaticSprite):
    def __init__(self, position: IntPoint) -> None:
        super().__init__(
            **{
                "name": "brick",
                "rect": Rect(position.x, position.y, 25, 10),
                "image_asset": "block_10x25.png",
            }
        )

    def handle_keyboard_event(self, event: Event) -> None:
        pass

    def handle_mouse_event(self, event: Event) -> None:
        pass

    def tick(self, colliding_sprites: List[AbstractSprite]) -> None:
        pass
