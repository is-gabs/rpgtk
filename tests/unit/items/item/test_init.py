from rpgtk.items.item import Item


def test_should_initiate_value_with_param():
    item = Item(
        name='Dagger',
        description='Just a dagger',
        value=10,
        weight=1
    )

    assert item.name == 'Dagger'
    assert item.description == 'Just a dagger'
    assert item.value == 10
    assert item.weight == 1
