"""
# Ordered Player

The ordered player, plays the first available move from top to bottom,
from left to right
"""
from supercat.classes import BasePlayer
from supercat.utils import boxes


class Player(BasePlayer):

    name = 'anti_ordered'

    def play(self, world, game, move_num, last_move):
        # lazy game
        if game is not None:
            # should play this game
            for row, col in boxes():
                if world[game][2-row, col] is None:
                    return game, (2-row, col)
        else:
            # free play!
            for grand_row, grand_col in boxes():
                if world[grand_row, grand_col]['owner'] is not None:
                    continue

                for row, col in boxes():
                    if world[grand_row, grand_col][2-row, col] is None:
                        return (grand_row, grand_col), (2-row, col)
        return None, None
