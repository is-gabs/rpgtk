from unittest import mock

from rpgtk.cards.deck import Deck


def test_should_return_len_of_cards_attribute():
    mock_cards = mock.MagicMock()

    deck = Deck(cards=mock_cards)

    assert deck.__len__() == mock_cards.__len__.return_value
