"""
Utility classes
"""
import argparse
from importlib import import_module
import os


class PlayerAction(argparse.Action):
    """Return a module"""
    def __init__(self, option_strings, dest, **kwargs):
        super(PlayerAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        built_players = []

        for value in values:
            if os.path.isfile(value):
                m = {}
                with open(value, mode='rb') as player_file:
                    exec(compile(player_file.read(), value, 'exec'), m)
                built_players.append(m['Player'])
            else:
                try:
                    m = import_module('supercat.players.' + value)
                    built_players.append(m.Player)
                except ModuleNotFoundError:
                    raise argparse.ArgumentError(
                        self, 'Not a valid default player or user defined'
                        ' player'
                    )

        setattr(namespace, self.dest, built_players)


class BasePlayer:
    """Represents a player"""

    name = 'base'

    def __init__(self, identity='X'):
        self.identity = identity

    def __str__(self):
        return self.name
