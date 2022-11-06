from dataclasses import dataclass
from typing import List

import pygame

from .sprites.ball import Ball
from .sprites.brick import Brick
from .sprites.paddle import Paddle


@dataclass
class World:  # pylint: disable=too-many-instance-attributes
    clock: pygame.time.Clock
    screen: pygame.surface.Surface
    background: pygame.surface.Surface
    ball: Ball
    paddle: Paddle
    bricks: List[Brick]
    font: pygame.sysfont.SysFont
    debug: bool = False

    def as_tuple(self):
        return (
            self.clock,
            self.screen,
            self.background,
            self.ball,
            self.paddle,
            self.bricks,
            self.font,
            self.debug,
        )
