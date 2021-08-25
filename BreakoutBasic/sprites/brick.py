from pygame.event import Event

from ..utils import Rect

from .sprite import AbstractSprite, StaticSprite


class Brick(StaticSprite):
    def __init__(self) -> None:
        super().__init__(
            **{
                "name": "brick",
                "rect": Rect(0, 0, 25, 10),
                "image_asset": "block_10x25.png",
            }
        )

    def handle_keyboard_event(self, event: Event) -> None:
        pass

    def handle_mouse_event(self, event: Event) -> None:
        pass

    def handle_collision(self, other: AbstractSprite) -> None:
        pass

    def tick(self) -> None:
        pass
