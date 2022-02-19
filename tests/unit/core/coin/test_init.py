from rpgtk.core import Coin


def test_should_initiate_with_2_sides():
    assert Coin.sides == ('head', 'tail')
