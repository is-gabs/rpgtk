import pytest

from rpgtk import Dice


def test_should_return_boolean():
    result = Dice().__ge__(Dice())

    assert isinstance(result, bool) is True


def test_should_raise_type_error_when_not_dice_object():
    with pytest.raises(TypeError) as err:
        Dice().__ge__(object)

    assert str(err.value) == 'Operation only allowed between Dice\'s instances'


def test_should_return_true_when_other_dice_is_lower():
    result = Dice(20).__ge__(Dice(2))

    assert result is True


def test_should_return_true_when_other_dice_is_equal():
    result = Dice(20).__ge__(Dice(20))

    assert result is True


def test_should_return_false_when_other_dice_is_greater():
    result = Dice(2).__ge__(Dice(20))

    assert result is False
