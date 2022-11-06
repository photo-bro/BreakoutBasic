import math
import random
import sys
from collections import defaultdict
from typing import Dict, List

import pygame
from pygame.surface import Surface

from .game_globals import WINDOW_SIZE
from .sprites import AbstractSprite, Ball, Brick, Paddle
from .utils import IntPoint
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

    font = pygame.sysfont.SysFont("monospace", 12)
    # test_title = font.render('Breakbasic !!', 1, (255, 255, 255))
    # background.blit(test_title, (0, 200))

    paddle = Paddle()
    paddle.rect.x = int(WIN_WIDTH / 2)
    paddle.rect.y = WIN_HEIGHT - 30

    ball = Ball()
    ball.rect.x = int(WIN_WIDTH / 2)
    ball.rect.y = WIN_HEIGHT - 100
    ball.velocity.x = random.uniform(-2 * math.pi, 2 * math.pi)
    ball.velocity.y = random.uniform(-2 * math.pi, 2 * math.pi)

    bricks: List[Brick] = []

    def destroy_brick_func(b: AbstractSprite):
        b.active = False
        if isinstance(b, Brick) and b in bricks:
            bricks.remove(b)

    brick_margin = 5
    brick_offset = 20
    for y in range(0, int((WIN_HEIGHT - 200) / (10 + brick_margin))):
        for x in range(0, int((WIN_WIDTH) / (25 + brick_margin) - 1)):
            b = Brick(
                position=IntPoint(
                    brick_offset + x * (25 + brick_margin),
                    brick_offset + y * (10 + brick_margin),
                )
            )
            b.destroy_func = destroy_brick_func
            bricks.append(b)
    print(f"Brick count: {len(bricks)}")
    return World(clock, screen, background, ball, paddle, bricks, font, debug)


def do_event_loop(world: World) -> bool:  # pylint: disable=too-many-locals
    (
        clock,
        screen,
        background,
        ball,
        paddle,
        bricks,
        font,
        game_debug,
    ) = world.as_tuple()
    sprites: List[AbstractSprite] = [paddle, ball, *bricks]
    pause: bool = False
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

        # Calculate collisions
        colliding_sprites: Dict[
            AbstractSprite, List[AbstractSprite]
        ] = calculate_colliding_sprites(ball, paddle, bricks)

        # Sprite tick
        for s in sprites:
            s.tick(colliding_sprites.get(s, []))

        # Render
        render_sprites(screen, background, sprites)
        if game_debug:
            background.fill(BLACK)
            ball_text = font.render(str(ball), 1, WHITE)
            background.blit(ball_text, (0, 0))
            paddle_text = font.render(str(paddle), 1, WHITE)
            background.blit(paddle_text, (0, 20))

        # pygame.event
        pygame.display.flip()

        clock.tick(60)  # limit to 60fps


def calculate_colliding_sprites(
    ball: Ball,
    paddle: Paddle,
    bricks: List[AbstractSprite],
) -> Dict[AbstractSprite, List[AbstractSprite]]:
    collided_sprite_dict: Dict[AbstractSprite, List[AbstractSprite]] = defaultdict(list)
    if ball.contains(paddle):
        collided_sprite_dict[ball].append(paddle)
        collided_sprite_dict[paddle].append(ball)
    collided_sprite_dict[ball].extend(b for b in bricks if ball.contains(b))
    return collided_sprite_dict


def render_sprites(
    screen: Surface, background: Surface, sprites: List[AbstractSprite]
) -> None:
    screen.blit(background, (0, 0))
    for s in sprites:
        if not s.active:
            continue
        # print(f'Sprite: {s.name} is at {s.position}')
        screen.blit(s.image, s.rect.position)
