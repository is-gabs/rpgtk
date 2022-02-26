from random import choice, randint
from typing import Optional

from rpgtk.exceptions import DiceException

SIDE_HEAD = 'head'
SIDE_TAIL = 'tail'


class Dice:
    '''
    The Dice object have some sides.

    Args:
        sides (int): The number of the sides of a dice instance.

    Attributes:
        last_roll (int|None): Result of the last roll of a dice instance.

    Don't let a dice fall from the table.
    '''
    def __init__(self, sides: Optional[int] = 6):
        if not isinstance(sides, int) or sides < 1:
            raise DiceException('Invalid sides value received.')

        self.sides = sides
        self.last_roll = None

    def roll(self) -> int:
        '''Returns a random Integer between one and the sides number.'''
        self.last_roll = randint(1, self.sides)
        return self.last_roll

    def __repr__(self) -> str:
        last_roll = f'[{self.last_roll}]' if self.last_roll else ''
        return f'D{self.sides}' + last_roll

    def __eq__(self, obj) -> bool:
        if not isinstance(obj, Dice):
            return False

        return self.sides == obj.sides


class Coin:
    '''
    The Coin object has only two sides.

    Keep it safe.
    '''
    sides = (SIDE_HEAD, SIDE_TAIL)

    @classmethod
    def flip(cls) -> str:
        '''Returns 'head' or 'tail'.'''
        return choice(cls.sides)
