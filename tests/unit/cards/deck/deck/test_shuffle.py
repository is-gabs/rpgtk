from unittest import mock

from rpgtk.cards.deck import Deck


@mock.patch('rpgtk.cards.deck.shuffle')
def test_should_call_shuffle_with_cards(mock_shuffle):
    mock_cards = mock.MagicMock()

    result = Deck(cards=mock_cards).shuffle()

    mock_shuffle.assert_called_once_with(mock_cards)
    assert result is None
