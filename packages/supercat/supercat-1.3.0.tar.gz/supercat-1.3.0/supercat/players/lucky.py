"""
# Random Player

like the ordered one, but randomizes its search
"""
from supercat.classes import BasePlayer
from supercat.utils import random_boxes


class Player(BasePlayer):

    name = 'lucky'

    def play(self, world, game, move_num, last_move):
        # lazy game
        if game is not None:
            # should play this game
            for row, col in random_boxes():
                if world[game][row, col] is None:
                    return game, (row, col)
        else:
            # free play!
            for grand_row, grand_col in random_boxes():
                if world[grand_row, grand_col]['owner'] is not None:
                    continue

                for row, col in random_boxes():
                    if world[grand_row, grand_col][row, col] is None:
                        return (grand_row, grand_col), (row, col)
        return None, None
