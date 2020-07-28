import os

from pygame.constants import (KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP,
                              MOUSEMOTION, MOUSEWHEEL)
from pygame.image import load


class AbstractSprite:
    """

    """

    def __init__(self, name, size, image_asset):
        self.name = name
        self.size = size
        self.image = load(os.path.join('assets/sprites', image_asset))
        self.position = (0, 0)

    def handle_event(self, event):
        if event.type in (KEYDOWN, KEYUP):
            self.handle_keyboard_event(event)
        elif event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEWHEEL):
            self.handle_mouse_event(event)

    def handle_keyboard_event(self, event):
        raise NotImplementedError()

    def handle_mouse_event(self, event):
        raise NotImplementedError()

    def handle_collision(self, other):
        raise NotImplementedError()

    def tick(self):
        pass
