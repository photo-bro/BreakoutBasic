from dataclasses import dataclass
from typing import List

import pygame

from .sprites.ball import Ball
from .sprites.paddle import Paddle
from .sprites.sprite import AbstractSprite


@dataclass
class World:
    clock: pygame.time.Clock
    screen: pygame.surface.Surface
    background: pygame.surface.Surface
    ball: Ball
    paddle: Paddle
    sprites: List[AbstractSprite]
    font: pygame.sysfont.SysFont
    debug: bool = False

    def as_tuple(self):
        return (
            self.clock,
            self.screen,
            self.background,
            self.ball,
            self.paddle,
            self.sprites,
            self.font,
            self.debug,
        )
