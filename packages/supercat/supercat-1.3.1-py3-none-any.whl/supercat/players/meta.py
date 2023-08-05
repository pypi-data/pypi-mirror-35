"""
# Ordered Player

The ordered player, plays the first available move from top to bottom,
from left to right
"""
from supercat.classes import BasePlayer
from supercat.utils import boxes


class Player(BasePlayer):

    name = 'meta'

    def play(self, world, game, move_num, last_move):
        # lazy game
        if game is not None:
            # should play this game
            for col, row in boxes():
                if world[game][row, 2-col] is None:
                    return game, (row, 2-col)
        else:
            # free play!
            for grand_row, grand_col in boxes():
                if world[2-grand_row, grand_col]['owner'] is not None:
                    continue

                for col, row in boxes():
                    if world[2-grand_row, grand_col][row, 2-col] is None:
                        return (2-grand_row, grand_col), (row, 2-col)
        return None, None
