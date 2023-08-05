"""
Utility classes
"""
import argparse
from importlib import import_module


class PlayerAction(argparse.Action):
    """Return a module"""
    def __init__(self, option_strings, dest, **kwargs):
        super(PlayerAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, list(map(
            lambda p: import_module('supercat.players.' + p),
            values
        )))


class BasePlayer:
    """Represents a player"""

    name = 'base'

    def __init__(self, identity='X'):
        self.identity = identity

    def __str__(self):
        return self.name
