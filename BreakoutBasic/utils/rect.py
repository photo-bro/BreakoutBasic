from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int

    @property
    def position(self) -> Tuple[int, int]:
        return (self.x, self.y)

    @property
    def volume(self) -> int:
        return self.w * self.h

    def contains(self, other: Rect) -> bool:
        if (
            self.x < other.x + other.w
            and self.x + self.w > other.x
            and self.y < other.y + other.h
            and self.y + self.h > other.y
        ):
            return True

        return False
