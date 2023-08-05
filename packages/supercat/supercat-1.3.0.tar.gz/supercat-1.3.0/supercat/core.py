"""
core functions
"""
import random
import time
import os
from supercat.utils import clean_world, is_owned, \
                           won_game, is_dead_world, \
                           is_dead_heat, csv, err
from datetime import datetime
from itertools import starmap

try:
    import pygame
    from pygame.locals import KEYDOWN, QUIT
    PYGAME_MODULE = True
except ImportError:
    print('pygame module not available')
    PYGAME_MODULE = False

ASSET_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    'assets'
))


def referi_func(
        players=None,
        fps=1,
        coin=False,
        capture_screen=False,
        no_render=False,
        wait=0,
        tournament=False,):
    render = not no_render

    if PYGAME_MODULE and render:
        pygame.init()
        screen = pygame.display.set_mode((395, 395))
        pygame.display.set_caption('Supercat referi')
        clock = pygame.time.Clock()
        board = pygame.image.load(os.path.join(ASSET_DIR, 'board.png'))
        icons = {
            "X": pygame.image.load(os.path.join(ASSET_DIR, 'square.png')),
            "O": pygame.image.load(os.path.join(ASSET_DIR, 'circle.png')),
        }
        big_icons = {
            "X": pygame.image.load(os.path.join(ASSET_DIR, 'square_big.png')),
            "O": pygame.image.load(os.path.join(ASSET_DIR, 'circle_big.png')),
            "R": pygame.image.load(os.path.join(ASSET_DIR, 'octo_big.png')),
        }

    pieces = ["X", "O", "R"]
    player1, player2 = list(starmap(
        lambda i, p: p(pieces[i]),
        enumerate(players)
    ))

    if player1.name == player2.name:
        name = player1.name
        assigns = {
            "X": name+'1',
            "O": name+'2',
        }
    else:
        assigns = {
            "X": player1.name,
            "O": player2.name,
        }

    players = [player1, player2]
    world = clean_world()

    turn = False
    move = 1
    game_should_play = None
    winner = 'R'
    last_move = None, None

    if coin and random.choice([0, 1]) == 1:
        players.reverse()
        pieces[0], pieces[1] = pieces[1], pieces[0]

    while True:
        player_name = assigns[pieces[turn]]

        if PYGAME_MODULE and render:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == 27:
                    # ESC key, exit game
                    return
                elif event.type == QUIT:
                    # Handles window close button
                    return

        # Make the player play
        game, pos = players[turn].play(
            world.copy(),
            game_should_play,
            move,
            last_move
        )

        # Handle surrenders
        if game is None:
            err("%s surrenders!" % player_name)
            break

        # Player made an invalid move
        if game_should_play is not None and game_should_play != game:
            err("%s did not play the game he should!" % player_name)
            break

        if world[game]['owner'] in pieces:
            err("%s attempted to play in a closed game!" % player_name)
            break

        # Not available boxes
        if world[game][pos] in pieces:
            err("%a attempted to play an already played box!" % player_name)
            break

        last_move = game, pos

        if not tournament:
            csv(
                str(move).rjust(2, ' '),
                player_name.rjust(15, ' '),
                *(game+pos)
            )

        # Set the world to the new status
        world[game][pos] = pieces[turn]

        if is_owned(world[game]):
            world[game]['owner'] = pieces[turn]
            err("%s owned game %s" % (player_name, game))

        if is_dead_heat(world[game]):
            world[game]['owner'] = 'R'
            err("%s killed the heat %s" % (player_name, game))

        game_should_play = pos if world[pos]['owner'] is None else None

        if PYGAME_MODULE and render:
            # Paint the board
            screen.fill((255, 255, 255))
            screen.blit(board, (0, 0))

            # Paint the game status
            for g_row in range(3):
                for g_col in range(3):
                    if world[g_row, g_col]['owner'] in pieces:
                        # draw a big one
                        coordinates = g_col*(105 + 30) + 10, \
                            g_row*(105+30) + 10
                        screen.blit(
                            big_icons[world[g_row, g_col]['owner']],
                            coordinates)
                        continue

                    for row in range(3):
                        for col in range(3):
                            if world[g_row, g_col][row, col] in pieces:
                                # draw a small one
                                coordinates = \
                                    g_col*(105 + 30) + \
                                    col*(25 + 15) + 10, \
                                    g_row*(105+30) + \
                                    row*(25 + 15) + 10
                                screen.blit(
                                    icons[world[g_row, g_col][row, col]],
                                    coordinates)

            pygame.display.flip()

        if won_game(world):
            err("%s wins!" % player_name)
            winner = player_name
            break

        elif is_dead_world(world):
            err("Game finished without a winner")
            break

        turn = not turn
        move += 1

        if PYGAME_MODULE and render:
            # tick to 1 fps
            clock.tick(fps)

    if capture_screen and PYGAME_MODULE and render:
        png_name = "caps/%s vs %s %s.png" % (
            player1.name,
            player2.name,
            datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
        )
        pygame.image.save(screen, png_name)
        print('game finish saved to %s' % png_name)

    if wait and PYGAME_MODULE and render:
        time.sleep(wait)

    return winner
