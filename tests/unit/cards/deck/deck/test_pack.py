import pytest

from rpgtk.cards.deck import Card, Deck, Positions


def test_should_append_card_on_cards_attribute():
    card = Card('value')
    deck = Deck()

    deck.pack(card=card)

    assert deck.cards == [card]


@pytest.mark.parametrize(
    ('position', 'index'), (
        (Positions.BEGIN, 0),
        (Positions.MIDDLE, 2),
        (Positions.END, -1)
    )
)
def test_should_append_card_on_specific_position(position, index):
    card = Card('value')
    deck = Deck(cards=[Card(str(x)) for x in range(4)])

    deck.pack(card=card, position=position)

    assert deck.cards[index] == card
