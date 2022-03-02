from unittest import mock

from rpgtk.cards.deck import Deck


def test_should_return_cards_getitem_return():
    mock_cards = mock.MagicMock()

    result = Deck(cards=mock_cards).__getitem__(1)

    assert result == mock_cards.__getitem__.return_value
    mock_cards.__getitem__.assert_called_once_with(1)
