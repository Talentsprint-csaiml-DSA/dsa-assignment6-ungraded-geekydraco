import pytest
from main import longest_box_sequence  # Replace 'your_module' with the actual module name

def test_empty_boxes():
    assert longest_box_sequence([]) == 0, "Failed on empty input"

def test_single_box():
    assert longest_box_sequence([(2, 2, 2)]) == 1, "Failed on single box input"

def test_two_fitting_boxes():
    assert longest_box_sequence([(1, 1, 1), (2, 2, 2)]) == 2, "Failed on two fitting boxes"

def test_complex_case():
    boxes = [(5, 4, 6), (6, 7, 8), (3, 2, 1), (4, 5, 6), (6, 5, 7)]
    assert longest_box_sequence(boxes) == 3, "Failed on complex input"

