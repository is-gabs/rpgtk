from rpgtk.cards.deck import Card


def test_should_initiate_value_with_param():
    card = Card(value='expected_value')

    assert card.value == 'expected_value'
