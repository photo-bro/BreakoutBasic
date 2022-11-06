import sys
from typing import List, Set

import pygame
from pygame.surface import Surface

from .game_globals import WINDOW_SIZE
from .sprites import AbstractSprite, Ball, Brick, Paddle
from .utils.colors import BLACK, WHITE
from .world import World

debug = True


def start_game() -> None:  # pylint: disable=too-many-locals
    pygame.init()

    world: World = create_world()
    while not do_event_loop(world):
        world = create_world()
        do_event_loop(world)
    sys.exit()


def create_world() -> World:
    clock = pygame.time.Clock()

    WIN_WIDTH, WIN_HEIGHT = WINDOW_SIZE

    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Breakout Basic - Josh Harmon")

    background = pygame.Surface(screen.get_size()).convert()
    background.fill(BLACK)

    font = pygame.sysfont.SysFont("monospace", 8)
    # test_title = font.render('Breakbasic !!', 1, (255, 255, 255))
    # background.blit(test_title, (0, 200))

    paddle = Paddle()
    paddle.rect.x = int(WIN_WIDTH / 2)
    paddle.rect.y = WIN_HEIGHT - 30

    ball = Ball()
    ball.rect.x = int(WIN_WIDTH / 2)
    ball.rect.y = WIN_HEIGHT - 100

    sprites: List[AbstractSprite] = [paddle, ball]

    def destroy_brick_func(b: AbstractSprite):
        return sprites.remove(b)

    # for y in range(0, int((WIN_HEIGHT - 200) / 20)):
    #     for x in range(0, int((WIN_WIDTH - 20) / 40)):
    #         b = Brick()
    #         b.rect.x = x * (b.rect.w + 10) + 40
    #         b.rect.y = y * (b.rect.h + 10) + 40
    #         b.destroy_func = destroy_brick_func
    #         sprites.append(b)

    return World(clock, screen, background, ball, paddle, sprites, font, debug)


def do_event_loop(world: World) -> bool:
    (
        clock,
        screen,
        background,
        ball,
        paddle,
        sprites,
        font,
        game_debug,
    ) = world.as_tuple()
    pause = False
    while True:
        # Events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_q:
                    return True
                if e.key == pygame.K_p:
                    pause = not pause
                if e.key == pygame.K_r:
                    print("RESET!!!")
                    return False

            if pause:
                break

            # Handle events
            for s in sprites:
                s.handle_event(e)

        if pause:
            continue

        # Handle collisions
        calculate_colliding_sprites(set(sprites))

        # Adjust positions
        for s in sprites:
            s.tick()

        # Render
        if game_debug:
            background.fill(BLACK)
            ball_text = font.render(str(ball), 1, WHITE)
            background.blit(ball_text, (0, 0))
            paddle_text = font.render(str(paddle), 1, WHITE)
            background.blit(paddle_text, (0, 20))
        render_sprites(screen, background, sprites)

        # pygame.event
        pygame.display.flip()

        clock.tick(60)  # limit to 60fps


def calculate_colliding_sprites(sprites: Set[AbstractSprite]) -> None:
    calculated_sprites: Set[AbstractSprite] = set()
    for s in sprites:
        if s in calculated_sprites:
            continue
        calculated_sprites.add(s)
        for o in sprites.difference(calculated_sprites):
            if s.contains(o):
                # print(f'Collision! Between: {s} and {o}')
                s.handle_collision(o)
                o.handle_collision(s)
                calculated_sprites.add(o)


def render_sprites(
    screen: Surface, background: Surface, sprites: List[AbstractSprite]
) -> None:
    screen.blit(background, (0, 0))
    for s in sprites:
        if not s.active:
            continue
        # print(f'Sprite: {s.name} is at {s.position}')
        screen.blit(s.image, s.rect.position)
