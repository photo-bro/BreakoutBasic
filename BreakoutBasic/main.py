import sys

import pygame

from sprites import Ball, Brick, Paddle

from game_globals import WINDOW_SIZE


def main():
    pygame.init()

    WIN_WIDTH, WIN_HEIGHT = WINDOW_SIZE

    black = 0, 0, 0

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Breakout Basic - Josh Harmon')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(black)

    # font = pygame.font.Font(None, 24)
    # test_title = font.render('Breakbasic !!', 1, (255, 255, 255))
    # background.blit(test_title, (0, 200))

    paddle = Paddle()
    paddle.position = (WIN_WIDTH / 2, WIN_HEIGHT - 30)

    ball = Ball()
    ball.position = (WIN_WIDTH / 2, WIN_HEIGHT / 2)

    bricks = []
    for y in range(0, int((WIN_HEIGHT - 200) / 20)):
        for x in range(0, int((WIN_WIDTH - 20) / 40)):
            b = Brick()
            bx, by = b.size
            b.position = (x * (bx + 10) + 40, y * (by + 10) + 40)
            bricks.append(b)

    sprites = [paddle, ball, *bricks]

    while True:

        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT or \
                    (e.type == pygame.KEYDOWN and e.key == pygame.K_q):
                sys.exit()

            # Handle events
            for s in sprites:
                s.handle_event(e)

        # Adjust positions
        for s in sprites:
            s.tick()

        # Handle collisions
        collided_sprites = []
        for s in sprites:
            if s in collided_sprites:
                continue
            for o in sprites:
                if s == o:
                    continue
                if o in collided_sprites:
                    continue
                if s.contains(o):
                    print(f'Collision! Between: {s} {s.position} and {o} {o.position}.')
                    s.handle_collision(o)
                    o.handle_collision(s)
                    collided_sprites.extend([s, o])

            # Paint
        screen.blit(background, (0, 0))
        for s in sprites:
            # print(f'Sprite: {s.name} is at {s.position}')
            screen.blit(s.image, s.position)

        # pygame.event
        pygame.display.flip()


if __name__ == '__main__':
    main()
