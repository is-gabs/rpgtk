from unittest import mock

from rpgtk.cards.deck import Deck


def test_should_return_pop_from_cards_attribute():
    mock_cards = mock.MagicMock()

    result = Deck(cards=mock_cards).draw()

    assert result == mock_cards.pop.return_value


def test_should_return_none_when_pop_raises_type_error():
    mock_cards = mock.MagicMock()
    mock_cards.pop.side_effect = IndexError

    result = Deck(cards=mock_cards).draw()

    assert result is None
