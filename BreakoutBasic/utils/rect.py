from __future__ import annotations

from typing import Optional


class Rect:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    @property
    def volume(self) -> int:
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rect):
            return self.width == other.width and self.height == other.height
        return False

    def __add__(self, other: Rect) -> Rect:
        return Rect(self.width + other.width, self.height + other.height)

    def __str__(self) -> str:
        return f'[{self.width} x {self.height}]'
