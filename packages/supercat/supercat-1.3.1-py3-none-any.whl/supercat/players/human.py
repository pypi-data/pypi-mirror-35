"""
# Human

like the ordered one, but randomizes its search
"""
from supercat.classes import BasePlayer
from supercat.utils import err


class Player(BasePlayer):

    name = 'human'

    def get_valid_coords(self, thing):
        while True:
            try:
                game = tuple(map(
                    lambda x: int(x),
                    input('%s: ' % thing).split(' ')
                ))
                for i in game:
                    if i not in (0, 1, 2):
                        raise ValueError()
                return game
            except ValueError:
                err('%s inválido' % thing)

    def game_name(self, row, col):
        rows = [
            'arriba',
            'centro',
            'abajo',
        ]
        cols = [
            'izquierda',
            'enmedio',
            'derecha',
        ]
        return rows[row] + ' ' + cols[col]

    def play(self, world, game, move_num, last_move):
        try:
            if game is None:
                game = self.get_valid_coords('Juego')
            else:
                err('Tienes que jugar el juego de %s' % self.game_name(*game))

            box = self.get_valid_coords('Movimiento')

            return game, box
        except KeyboardInterrupt:
            return None, None
