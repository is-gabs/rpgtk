from rpgtk import Dice


def test_should_return_false_when_not_a_dice_instance():
    assert Dice().__eq__(object) is False


def test_should_return_true_when_same_number_of_sides():
    dice = Dice(sides=10)

    assert Dice(sides=10).__eq__(dice) is True
