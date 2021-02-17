from dataclasses import dataclass
from random import randint

from cortex.dice.constants import DIE_FACES_NUMBERS
from cortex.dice.exceptions import (DieFacesValueException,
                                    DieOperationException)


@dataclass
class Die:
    faces: int
    result: int = 0

    def __init__(self, faces=4):
        if faces not in DIE_FACES_NUMBERS:
            raise DieFacesValueException()

        self.faces = faces

    def roll(self) -> int:
        self.result = randint(1, self.faces)
        return self.result

    def step_up(self):
        index = DIE_FACES_NUMBERS.index(self.faces)
        try:
            self.faces = DIE_FACES_NUMBERS[index + 1]
        except IndexError:
            raise DieOperationException('Not possible to step up this dice')

    @property
    def is_hitch(self):
        return self.result == 1
