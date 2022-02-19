from random import randint
from typing import Optional

from rpgtk.exceptions import DiceException


class Dice:
    def __init__(self, sides: Optional[int] = 6):
        if not isinstance(sides, int) or sides < 1:
            raise DiceException('Invalid sides value received.')

        self.sides = sides
        self.last_roll = None

    def roll(self):
        self.last_roll = randint(1, self.sides)
        return self.last_roll
