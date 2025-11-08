import pytest
from jar import Jar

def test_init_and_capacity():
    """Test initialization and invalid capacities."""
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("abc")

def test_str():
    """Test string representation of cookies."""
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    """Test adding cookies to the jar."""
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    """Test removing cookies from the jar."""
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(5)
