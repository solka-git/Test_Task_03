import pytest
from Password import Password


def test_01():
    assert Password.validate('ghjrtFG67&*fffff') == True
    assert Password.validate('1234') == False
    assert Password.validate('1234test') == False
    assert Password.validate('!1234test') == False
    assert Password.validate('1234FFFtegg№') == False


def test_02():
    assert type(Password.generate(17)) is str
    assert Password.validate(Password.generate(12)) == False
    assert Password.validate(Password.generate(18)) == True
