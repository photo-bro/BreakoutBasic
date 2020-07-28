import sprites
from game_globals import WINDOW_SIZE


class Ball(sprites.AbstractSprite):
    _speed = 5
    _dir_x = 1
    _dir_y = 1

    def __init__(self):
        super().__init__(**{
            'name': 'ball',
            'size': (5, 5),
            'image_asset': 'ball_5x5.png'
        })

    def handle_keyboard_event(self, event):
        pass

    def handle_mouse_event(self, event):
        pass

    def handle_collision(self, other):
        if isinstance(other, sprites.Brick):
            print(f'Collision with a brick at: ({self.position})')
        if isinstance(other, sprites.Paddle):
            print(f'Collision with the paddle at: ({self.position})')

    def move(self):
        window_x, window_y = WINDOW_SIZE
        size_x, size_y = self.size
        x, y = self.position

        vel_x = (self._speed * self._dir_x)
        vel_y = (self._speed * self._dir_y)

        if x + size_x + vel_x > window_x:
            x = window_x - size_x
            self._dir_x = -1
        if y + size_y + vel_y > window_y:
            y = window_y - size_y
            self._dir_y = -1

        if x + vel_x < 0:
            x = 0
            self._dir_x = 1
        if y + vel_y < 0:
            y = 0
            self._dir_y = 1

        self.position = (x + vel_x, y + vel_y)

    def tick(self):
        self.move()
