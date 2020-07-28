from sprites import StaticSprite


class Brick(StaticSprite):

    def __init__(self):
        super().__init__(**{
            'name': 'brick',
            'size': (25, 10),
            'image_asset': 'block_10x25.png'
        })

    def handle_keyboard_event(self, event):
        pass

    def handle_mouse_event(self, event):
        pass

    def tick(self):
        pass
