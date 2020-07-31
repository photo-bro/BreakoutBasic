from __future__ import annotations

import math
from typing import Tuple


class Vector2d:
    def __init__(self, magnitude: float, direction: float):
        self.magnitude = magnitude
        self.direction = direction

    @property
    def x(self) -> float:
        return math.cos(self.direction)

    @property
    def y(self) -> float:
        return math.sin(self.direction)

    def add(self, other: Vector2d) -> Vector2d:
        mx, my = (self.x + other.x, self.y + other.y)
        new_mag = math.sqrt(mx**2, my**2)
        new_dir = math.asin(mx/my)
        return Vector2d(new_mag, new_dir)

    def mirror_x(self):
        self.direction = math.pi - self.direction
    
    def mirror_y(self):
        self.direction =-self.direction

    @property
    def direction_degrees(self):
        return self.direction * (180 / math.pi)

    def __str__(self):
        return f'{self.magnitude} : {self.direction:.4f}rad {self.direction_degrees:.4f}degr'
