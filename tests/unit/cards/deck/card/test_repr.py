from rpgtk.cards.deck import Card


def test_should_return_value():
    result = Card(value='expected_value').__repr__()

    assert result == 'expected_value'


def test_should_return_cover_when_is_flipped():
    result = Card(
        value='expected_value',
        is_flipped=True,
        cover='cover'
    ).__repr__()

    assert result == 'cover'
