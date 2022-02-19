from unittest import mock

from rpgtk.core import Dice


@mock.patch('rpgtk.core.randint')
def test_should_return_randint_result(
    mock_randint
):
    dice = Dice(sides=10)

    result = dice.roll()

    assert result == mock_randint.return_value
    mock_randint.assert_called_once_with(1, 10)
    assert dice.last_roll == result
