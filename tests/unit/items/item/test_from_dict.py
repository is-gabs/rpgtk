from rpgtk.items.item import Item


def test_should_return_expected_object():
    item = Item.from_dict(
        payload={
            'name': 'Dagger',
            'description': 'Just a dagger',
            'value': 10,
            'weight': 1
        }
    )

    assert item.name == 'Dagger'
    assert item.description == 'Just a dagger'
    assert item.value == 10
    assert item.weight == 1
