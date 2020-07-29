import sprites
from game_globals import WINDOW_SIZE


class Ball(sprites.DynamicSprite):

    def __init__(self):
        super().__init__(**{
            'initial_speed': 5,
            'initial_direction': (1, 1),
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
            other.destroy()

        if isinstance(other, sprites.Paddle):
            pass
        self.bounce(other)

    def bounce(self, other):
        dx, dy = self.direction
        x, y = self.position
        ox, oy = other.position
        sx, sy = other.size

        if oy == y <= oy + sy:  # inside vertically
            dy = -dy
        if ox == x <= ox + sx:  # inside horizontally
            dx = -dx

        self.direction = (dx, dy)

    def move(self):
        window_x, window_y = WINDOW_SIZE
        size_x, size_y = self.size
        x, y = self.position
        dir_x, dir_y = self.direction
        vel_x, vel_y = self.velocity

        if x + size_x + vel_x > window_x:
            x = window_x - size_x
            dir_x = -1
        if y + size_y + vel_y > window_y:
            y = window_y - size_y
            dir_y = -1

        if x + vel_x < 0:
            x = 0
            dir_x = 1
        if y + vel_y < 0:
            y = 0
            dir_y = 1

        self.position = (x + vel_x, y + vel_y)
        self.direction = (dir_x, dir_y)

    def tick(self):
        self.move()
