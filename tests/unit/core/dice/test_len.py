from rpgtk import Dice


def test_should_return_last_roll():
    dice = Dice()
    dice.last_roll = 8
    assert dice.__len__() == 8
