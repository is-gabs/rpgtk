from rpgtk.cards.deck import Card


def test_should_alternate_is_flippled_attribute():
    card = Card('value', is_flipped=True)

    card.flip()

    assert card.is_flipped is False

    card.flip()

    assert card.is_flipped is True
