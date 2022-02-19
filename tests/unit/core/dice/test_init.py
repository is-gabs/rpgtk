import pytest

from rpgtk.core import Dice
from rpgtk.exceptions import DiceException


@pytest.mark.parametrize(
    'invalid_value', (
        -1, 'a', 0.5
    )
)
def test_should_raise_dice_exception_when_invalid_sides(invalid_value):
    with pytest.raises(DiceException) as err:
        Dice(sides=-1)

    assert str(err.value) == 'Invalid sides value received.'


def test_should_initiate_last_roll_attr_with_none_value():
    assert Dice().last_roll is None
