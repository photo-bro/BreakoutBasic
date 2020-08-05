from __future__ import annotations

import math
from typing import Tuple


class Vector2d:
    magnitude: float
    direction: float  # in radians

    def __init__(self, magnitude: float, direction: float) -> None:
        self.magnitude = magnitude
        self.direction = direction

    @property
    def x(self) -> float:
        return math.cos(self.direction) * self.magnitude

    @property
    def y(self) -> float:
        return math.sin(self.direction) * self.magnitude

    def add(self, other: Vector2d) -> Vector2d:
        mx, my = (self.x + other.x, self.y + other.y)
        new_mag = math.sqrt(mx**2 + my**2)
        new_dir = math.asin(mx/my)
        return Vector2d(new_mag, new_dir)

    def normalize_direction(self) -> None:
        if 0 > self.direction > 2 * math.pi:
            self.direction %= math.pi

    def mirror_x(self) -> None:
        self.normalize_direction()
        self.direction = math.pi - self.direction

    def mirror_y(self) -> None:
        self.normalize_direction()
        self.direction = -self.direction

    @property
    def direction_degrees(self) -> float:
        return self.direction * (180 / math.pi)

    def __str__(self) -> str:
        return f' {self.magnitude:.2f} : {self.direction:.2f}rad {self.direction_degrees:.0f}˚'
