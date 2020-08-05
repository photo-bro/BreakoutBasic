from __future__ import annotations

from typing import Optional, Tuple


class Rect:
    x: int
    y: int
    w: int
    h: int

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @property
    def position(self) -> Tuple[int, int]:
        return (self.x, self.y)

    @property
    def volume(self) -> int:
        return self.w * self.h

    def contains(self, other: Rect) -> bool:
        if self.x < other.x + other.w and self.x + self.w > other.x and \
                self.y < other.y + other.h and self.y + self.h > other.y:
            return True

        return False

    def __str__(self) -> str:
        return f'({self.x}, {self.y}):[{self.w} x {self.h}]'
