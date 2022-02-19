from rpgtk.exceptions import DiceException, RPGTKBaseException


def test_should_extends_rpgtk_base_exception():
    assert issubclass(DiceException, RPGTKBaseException) is True
