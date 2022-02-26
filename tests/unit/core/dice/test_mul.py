from unittest import mock

import pytest

from rpgtk import Dice


def test_should_raise_type_error_when_not_int():
    with pytest.raises(TypeError) as err:
        Dice().__mul__(object)

    assert str(err.value) == 'Unsupported operand type(s) for *'


@mock.patch.object(Dice, 'roll')
def test_should_call_roll_multiple_times(mock_roll):
    result = Dice(sides=10).__mul__(3)

    assert mock_roll.call_count == 3
    assert result == [mock_roll.return_value] * 3
