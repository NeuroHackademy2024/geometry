from geometry.circle import calculate_area
from math import pi

def test_calculate_area():
    assert calculate_area(1) == pi, "Calculation did not work"

def test_calculate_area_zero():    
    assert calculate_area(0) == 0, "Calculation did not work"

def test_calculate_circ():
    assert calculate_circ(1) == 2 * pi