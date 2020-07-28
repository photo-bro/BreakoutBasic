import sys

import pygame

from game_globals import WINDOW_SIZE
from sprites import Paddle, Ball


def main():
    pygame.init()

    WIN_WIDTH, WIN_HEIGHT = WINDOW_SIZE

    black = 0, 0, 0

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Breakout Basic - Josh Harmon')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(black)

    font = pygame.font.Font(None, 24)
    test_title = font.render('Breakbasic !!', 1, (255, 255, 255))
    background.blit(test_title, (0, 200))

    paddle = Paddle()
    paddle.position = (WIN_WIDTH / 2, WIN_HEIGHT - 30)

    ball = Ball()
    ball.position = (WIN_WIDTH / 2, WIN_HEIGHT / 2)

    sprites = [paddle, ball]

    while True:

        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            # Handle events
            for s in sprites:
                s.handle_event(e)

        # Adjust positions
        for s in sprites:
            s.tick()

        # Handle collisions

        # Paint
        screen.blit(background, (0, 0))
        for s in sprites:
            # print(f'Sprite: {s.name} is at {s.position}')
            screen.blit(s.image, s.position)

        # pygame.event
        pygame.display.flip()


if __name__ == '__main__':
    main()
