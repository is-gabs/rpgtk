from unittest import mock

from rpgtk.cards.deck import Card, Deck


def test_should_initiate_cards_with_param():
    expected_cards = [Card('card')]

    deck = Deck(cards=expected_cards)

    assert deck.cards == expected_cards


@mock.patch('rpgtk.cards.deck.Card')
@mock.patch('rpgtk.cards.deck.DEFAULT_CARDS_VALUES')
def test_should_initiate_cards_with_default_cards(
    mock_default_cards,
    mock_card
):
    mock_default_cards.__iter__.return_value = ('card', )

    deck = Deck()

    mock_card.assert_called_once_with(value='card')
    assert deck.cards == [mock_card.return_value]
