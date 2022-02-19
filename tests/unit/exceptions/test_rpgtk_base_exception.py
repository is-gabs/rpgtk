from rpgtk.exceptions import RPGTKBaseException


def test_should_extends_exception():
    assert issubclass(RPGTKBaseException, Exception) is True
