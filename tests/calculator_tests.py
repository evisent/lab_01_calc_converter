import pytest

from toolkit.calculator import calculation
from toolkit.errors import Error

# Positive tests

def test_addition():
    assert calculation("2 + 2") == 4

def test_subtraction():
    assert calculation("10 - 3") == 7

def test_subtraction2():
    assert calculation("2 - 3 - 4") == -5

def test_multiplication():
    assert calculation("3 * 4") == 12

def test_division():
    assert calculation("10 / 4") == 2.5

def test_division2():
    assert calculation("100 / 10 / 2") == 5

def test_priority_multiplication():
    assert calculation("2 + 2 * 3") == 8

def test_priority_brackets():
    assert calculation("(2 + 2) * 3") == 12

def test_negative_operand():
    assert calculation("-5 + 3") == -2

def test_complex_expression():
    assert calculation("-2 * (3 + 4) / (5 - 2)") == pytest.approx(-14 / 3)


# Negative tests

def test_empty():
    with pytest.raises(Error):
        calculation("")

def test_spaces():
    with pytest.raises(Error):
        calculation("   ")

def test_missing_operand1():
    with pytest.raises(Error):
        calculation("2 +")

def test_missing_operand2():
    with pytest.raises(Error):
        calculation("*2")

def test_missing_operand3():
    with pytest.raises(Error):
        calculation("2 */ 3")

def test_unclosed_bracket():
    with pytest.raises(Error):
        calculation("(2 + 3")

def test_extra_bracket():
    with pytest.raises(Error):
        calculation("2 + 3)")

def test_missing_operator():
    with pytest.raises(Error):
        calculation("2 3")

def test_division_by_zero():
    with pytest.raises(Error):
        calculation("1 / 0")

def test_unknown_symbols1():
    with pytest.raises(Error):
        calculation("abc")

def test_unknown_symbols2():
    with pytest.raises(Error):
        calculation("2 + a")

def test_wrong_number():
    with pytest.raises(Error):
        calculation("2..5")