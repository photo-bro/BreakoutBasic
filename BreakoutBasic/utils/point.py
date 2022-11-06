from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass
class FloatPoint:
    x: float
    y: float

    @property
    def position(self) -> Tuple[float, float]:
        return (self.x, self.y)

    def __add__(self, other: FloatPoint) -> FloatPoint:
        return FloatPoint(self.x + other.x, self.y + other.y)


@dataclass
class IntPoint:
    x: int
    y: int

    @property
    def position(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def __add__(self, other: IntPoint) -> IntPoint:
        return IntPoint(self.x + other.x, self.y + other.y)
