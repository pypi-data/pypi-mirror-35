"""
Utility module, functions for working with the world
"""
import random
from functools import partial
import sys

err = partial(print, file=sys.stderr)
csv = partial(print, sep=', ')


def oponent(self, identity):
    return chr(-1*ord(identity) + 167)


def boxes():
    return tuple((row, col) for row in range(3) for col in range(3))


def corners():
    return tuple((row, col) for row in (0, 2) for col in (0, 2))


def shuffle(iterable):
    items = list(iterable)[:]
    random.shuffle(items)
    return items


def random_boxes():
    return shuffle((row, col) for row in range(3) for col in range(3))


def clean_world():
    world = {
        game: {
            box: None
            for box in boxes()
        }
        for game in boxes()
    }

    for game in boxes():
        world[game]['owner'] = None

    return world


def is_owned(game):
    # check rows
    for row in range(3):
        if game[row, 0] is None:
            continue
        if game[row, 0] == game[row, 1] == game[row, 2]:
            return True
    # check cols
    for col in range(3):
        if game[0, col] is None:
            continue
        if game[0, col] == game[1, col] == game[2, col]:
            return True
    # check diagonals
    if game[0, 0] is not None and game[0, 0] == game[1, 1] == game[2, 2]:
        return True
    return game[0, 2] is not None and game[0, 2] == game[1, 1] == game[2, 0]


def is_dead_heat(game):
    # check if there are empty boxes
    filled_boxes = 0
    for row, col in boxes():
        filled_boxes += game[row, col] is not None
    if filled_boxes < 9:
        return False

    # check rows
    for row in range(3):
        if game[row, 0] == game[row, 1] == game[row, 2]:
            return False
    # check cols
    for col in range(3):
        if game[0, col] == game[1, col] == game[2, col]:
            return False
    # check diagonals
    if game[0, 0] == game[1, 1] == game[2, 2]:
        return False
    return not (game[0, 2] == game[1, 1] == game[2, 0])


def is_dead_world(world):
    # check if there are empty boxes
    filled_boxes = 0
    for row, col in boxes():
        filled_boxes += world[row, col]['owner'] is not None
    if filled_boxes < 9:
        return False

    # check rows
    for row in range(3):
        if world[row, 0]['owner'] != 'R' and \
           world[row, 0] == world[row, 1] == world[row, 2]:
            return False
    # check cols
    for col in range(3):
        if world[0, col] != 'R' and \
           world[0, col] == world[1, col] == world[2, col]:
            return False
    # check diagonals
    if world[0, 0] != 'R' and world[0, 0] == world[1, 1] == world[2, 2]:
        return False
    return world[0, 2] != 'R' and not \
        (world[0, 2] == world[1, 1] == world[2, 0])


def won_game(world):
    # check rows
    for row in range(3):
        if world[row, 0]['owner'] in [None, 'R']:
            continue
        if world[row, 0]['owner'] == \
           world[row, 1]['owner'] == \
           world[row, 2]['owner']:
            return True
    # check cols
    for col in range(3):
        if world[0, col]['owner'] in [None, 'R']:
            continue
        if world[0, col]['owner'] == \
           world[1, col]['owner'] == \
           world[2, col]['owner']:
            return True
    # check diagonals
    if world[0, 0]['owner'] not in [None, 'R'] and \
       world[0, 0]['owner'] == \
       world[1, 1]['owner'] == \
       world[2, 2]['owner']:
        return True
    return world[0, 2]['owner'] not in [None, 'R'] and \
        world[0, 2]['owner'] == \
        world[1, 1]['owner'] == \
        world[2, 0]['owner']
