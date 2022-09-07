from rpgtk.items.item import Item


def test_should_return_expected_dict():
    item = Item(
        name='Dagger',
        description='Just a dagger',
        value=10,
        weight=1
    )

    result = item.to_dict()

    assert result == {
        'name': 'Dagger',
        'description': 'Just a dagger',
        'value': 10,
        'weight': 1
    }
