import pytest

from toolkit.converter import convertation
from toolkit.errors import Error

# Positive tests for length

def test_mm_to_cm():
    assert convertation(10, "mm", "cm") == 1

def test_cm_to_mm():
    assert convertation(1, "cm", "mm") == 10

def test_m_to_cm():
    assert convertation(1, "m", "cm") == 100

def test_km_to_m():
    assert convertation(1, "km", "m") == 1000

def test_km_to_mm():
    assert convertation(1, "km", "mm") == 1_000_000

def test_mm_to_m():
    assert convertation(1000, "mm", "m") == 1


# Positive tests for weight

def test_kg_to_g():
    assert convertation(1, "kg", "g") == 1000

def test_g_to_kg():
    assert convertation(500, "g", "kg") == 0.5


# Positive tests for temperature

def test_c_to_f():
    assert convertation(0, "c", "f") == 32

def test_f_to_c():
    assert convertation(32, "f", "c") == 0

def test_c_to_k():
    assert convertation(0, "c", "k") == 273.15

def test_k_to_c():
    assert convertation(273.15, "k", "c") == 0

def test_f_to_k():
    assert convertation(32, "f", "k") == pytest.approx(273.15)


# Positive different cases

def test_dif_cases1():
    assert convertation(1, "M", "CM") == 100

def test_dif_cases2():
    assert convertation(1, "Km", "M") == 1000


# Negative tests

def test_length_to_weight():
    with pytest.raises(Error):
        convertation(1, "m", "g")

def test_weight_to_length():
    with pytest.raises(Error):
        convertation(1, "kg", "km")

def test_unknown_unit():
    with pytest.raises(Error):
        convertation(1, "xyz", "m")

def test_temperature1():
    with pytest.raises(Error):
        convertation(-274, "c", "k")

def test_temperature2():
    with pytest.raises(Error):
        convertation(-0.1, "k", "c")
