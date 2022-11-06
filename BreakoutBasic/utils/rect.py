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
    def left(self) -> int:
        return self.x

    @property
    def right(self) -> int:
        return self.x + self.w - 1

    @property
    def top(self) -> int:
        return self.y

    @property
    def bottom(self) -> int:
        return self.y + self.h - 1

    @property
    def position(self) -> Tuple[int, int]:
        return (self.x, self.y)

    @property
    def volume(self) -> int:
        return self.w * self.h

    def intersects(self, other: Rect) -> bool:
        return (
            self.left <= other.right
            and other.left <= self.right
            and self.top <= other.bottom
            and other.top <= self.bottom
        )

    def intersected(self, other: Rect) -> Rect:
        nl = min(self.left, other.left)
        nr = max(self.right, other.right)
        nt = min(self.top, other.top)
        nb = max(self.bottom, other.bottom)

        if nl > nr or nt > nb:
            return Rect(0, 0, 0, 0)

        return Rect(
            x=nl,
            y=nt,
            w=nr - nl + 1,
            h=nb - nt + 1,
        )
