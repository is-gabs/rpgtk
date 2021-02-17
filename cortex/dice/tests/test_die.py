import pytest
from dataclasses import is_dataclass
import mock


from cortex.dice.exceptions import DieFacesValueException


@pytest.fixture
def die_class():
    from cortex.dice.die import Die

    return Die


@pytest.fixture
def allowed_faces_numbers():
    with mock.patch(
            'cortex.dice.die.DIE_FACES_NUMBERS'
    ) as mocked_constant:
        mocked_constant.return_value = [1]
        yield mocked_constant


def test_should_exist_a_die_class_at_die_module():
    try:
        from cortex.dice.die import Die
    except ImportError:
        pytest.fail('Cannot import Die class')


def test_die_class_should_be_a_dataclass(die_class):
    assert is_dataclass(die_class)


def test_die_class_should_raise_exception_for_not_allowed_number_of_faces(
    die_class,
    allowed_faces_numbers
):
    with pytest.raises(DieFacesValueException):
        die_class(4)


def test_default_die_result_must_be_zero(die_class):
    assert die_class().result == 0


def test_after_roll_the_result_attribute_must_be_updated(die_class):
    die = die_class()
    result = die.roll()
    assert die.result == result


def test_default_die_number_of_faces_attribute_must_be_4(die_class):
    assert die_class().faces == 4


def test_die_is_hitch_property_should_return_true_when_result_is_1(die_class):
    die = die_class()
    die.result = 1
    assert die.is_hitch is True
