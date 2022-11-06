import math
from typing import List

from pygame.event import Event

from ..game_globals import WINDOW_SIZE
from ..utils import Rect
from .brick import Brick
from .paddle import Paddle
from .sprite import AbstractSprite, DynamicSprite


class Ball(DynamicSprite):
    def __init__(self) -> None:
        super().__init__(
            velocity=None,
            **{
                "name": "ball",
                "rect": Rect(0, 0, 5, 5),
                "image_asset": "ball_5x5.png",
            },
        )

    def handle_keyboard_event(self, event: Event) -> None:
        pass

    def handle_mouse_event(self, event: Event) -> None:
        pass

    def tick(self, colliding_sprites: List[AbstractSprite]) -> None:
        nx, ny = self.rect.position
        nw, nh = self.rect.w, self.rect.h
        vx, vy = self.velocity.position

        nx += vx  # type: ignore
        ny += vy  # type: ignore

        window_x, window_y = WINDOW_SIZE

        # Wall collisions
        # Left and right walls
        if nx <= 0 or nx > window_x - nw:
            nx = self.rect.x
            vx *= -1
        # Top and bottom wall
        if ny <= 0 or ny > window_y - nh:
            ny = self.rect.y
            vy *= -1

        for other in colliding_sprites:
            if isinstance(other, Paddle):
                if self.rect.y < ny:
                    ny = self.rect.y
                vy = math.fabs(vy) * -1
                distance_to_middle_paddle = nx - (other.rect.x + other.rect.w / 2)
                relative_impact_point = distance_to_middle_paddle / other.rect.w
                vx = relative_impact_point * 7

            if isinstance(other, Brick):
                overlap_rect = self.rect.intersected(other.rect)
                if overlap_rect.w < overlap_rect.h:
                    nx = self.rect.x
                    vx *= -1
                else:
                    ny = self.rect.y
                    vy *= -1

                other.destroy()

        self.rect.x = nx
        self.rect.y = ny
        self.velocity.x = vx
        self.velocity.y = vy
