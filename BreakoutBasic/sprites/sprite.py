import os

from pygame.constants import (KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP,
                              MOUSEMOTION, MOUSEWHEEL)
from pygame.image import load


class AbstractSprite:

    def __init__(self, name, size, image_asset):
        self.name = name
        self.size = size
        self.image = load(os.path.join('assets/sprites', image_asset))
        self.position = (0, 0)

    def handle_event(self, event):
        pass

    def tick(self):
        pass

    def handle_collision(self, other):
        pass

    def contains(self, other):
        assert issubclass(type(other), AbstractSprite)
        x, y = self.position
        len_x, len_y = self.size
        ox, oy = other.position
        olen_x, olen_y = other.size

        if ox >= x and ox + olen_x <= x + len_x:
            pass
        else:
            return False

        if oy >= y and oy + olen_y <= y + len_y:
            return True

        return False


class StaticSprite(AbstractSprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DynamicSprite(AbstractSprite):
    speed = 0
    direction = (0, 0)

    def __init__(self, initial_speed=None, initial_direction=None, * args, **kwargs):
        if initial_speed:
            self.speed = initial_speed
        if initial_direction:
            self.direction = initial_direction
        super().__init__(*args, **kwargs)

    @property
    def velocity(self):
        dir_x, dir_y = self.direction
        return (self.speed * dir_x, self.speed * dir_y)

    def handle_event(self, event):
        if event.type in (KEYDOWN, KEYUP):
            self.handle_keyboard_event(event)
        elif event.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEWHEEL):
            self.handle_mouse_event(event)

    def handle_keyboard_event(self, event):
        raise NotImplementedError()

    def handle_mouse_event(self, event):
        raise NotImplementedError()
