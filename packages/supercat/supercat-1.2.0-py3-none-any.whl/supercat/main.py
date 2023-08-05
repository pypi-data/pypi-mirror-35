#!/usr/bin/env python
"""
The referi module
"""
import argparse
from supercat.core import referi_func
from supercat.classes import PlayerAction


def referi():
    parser = argparse.ArgumentParser(
        prog="referi",
        description='Supercat referi',
        epilog="""
        lets play!
        """
    )

    parser.add_argument(
        'players',
        metavar='PLAYER1 PLAYER2',
        nargs=2,
        type=str,
        help='players to play',
        action=PlayerAction,
    )
    parser.add_argument(
        '-f', '--fps',
        metavar='NUM',
        type=int,
        help='fps at with the game should play',
        default=1,
    )
    parser.add_argument(
        '-c', '--coin',
        action='store_true',
        help='should the referi flip a coin?',
        default=False,
    )
    parser.add_argument(
        '-s', '--capture-screen',
        action='store_true',
        help='take a screenshot of the final game',
        default=False,
    )
    parser.add_argument(
        '-n', '--no-render',
        action='store_true',
        help='Do not render the pygame GUI, just compute the game',
        default=False,
    )
    parser.add_argument(
        '-w', '--wait',
        metavar='SECONDS',
        type=int,
        help='wait before game disapears',
        default=0,
    )

    args = parser.parse_args()

    referi_func(**vars(args))
