from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar1 = Jar()
    jar1.deposit(2)
    assert str(jar1) == "🍪🍪"

def test_deposit():
    jar2 = Jar()
    jar2.deposit(5)
    assert jar2.size == 5
    with pytest.raises(ValueError):
        jar2.deposit(12)

def test_withdraw():
    jar3 = Jar()
    jar3.deposit(5)
    jar3.withdraw(3)
    assert jar3.size == 2
    with pytest.raises(ValueError):
        jar3.withdraw(12)
