import pygame

from .sprite import StaticSprite


class Brick(StaticSprite):

    def __init__(self) -> None:
        super().__init__(**{
            'name': 'brick',
            'size': (25, 10),
            'image_asset': 'block_10x25.png'
        })

    def handle_keyboard_event(self, event: pygame.event) -> None:
        pass

    def handle_mouse_event(self, event: pygame.event) -> None:
        pass

    def handle_collision(self, other: pygame.event) -> None:
        pass

    def tick(self) -> None:
        pass
