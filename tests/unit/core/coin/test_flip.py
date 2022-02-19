from unittest import mock

from rpgtk.core import Coin


@mock.patch('rpgtk.core.choice')
def test_should_return_choice_result(
    mock_choice
):
    result = Coin.flip()

    assert result == mock_choice.return_value
    mock_choice.assert_called_once_with(Coin.sides)
