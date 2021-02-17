import pytest


@pytest.fixture
def die_exception():
    from cortex.dice.exceptions import DieException
    return DieException


def test_should_exists_a_die_base_exception():
    try:
        from cortex.dice.exceptions import DieException  # noqa
    except ImportError:
        pytest.fail('Cannot import DieException')


def test_die_exception_should_be_a_exception(die_exception):
    assert issubclass(die_exception, Exception)


def test_should_exists_a_die_faces_value_exception():
    try:
        from cortex.dice.exceptions import DieFacesValueException  # noqa
    except ImportError:
        pytest.fail('Cannot import DieFacesValueException')
