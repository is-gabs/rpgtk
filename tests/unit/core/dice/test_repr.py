from rpgtk.core import Dice


def test_should_return_str():
    result = Dice().__repr__()

    assert isinstance(result, str)


def test_should_return_formated_string():
    result = Dice(sides=6).__repr__()

    assert result == 'D6'


def test_should_return_formated_string_when_last_roll():
    dice = Dice(10)
    dice.last_roll = 6

    result = dice.__repr__()

    assert result == 'D10[6]'
