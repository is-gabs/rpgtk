import pytest

from rpgtk import Dice


def test_should_return_boolean():
    result = Dice().__gt__(Dice())

    assert isinstance(result, bool) is True


def test_should_raise_type_error_when_not_dice_object():
    with pytest.raises(TypeError) as err:
        Dice().__gt__(object)

    assert str(err.value) == 'Operation only allowed between Dice\'s instances'


def test_should_return_false_when_other_dice_is_greater():
    result = Dice(sides=2).__gt__(Dice(sides=20))

    assert result is False


def test_should_return_true_when_other_dice_is_lower():
    result = Dice(sides=20).__gt__(Dice(sides=2))

    assert result is True
