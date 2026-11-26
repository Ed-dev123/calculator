from batch_calculator import process_calculation
a = 4.0
b = 5.0
c = 0.0
def test_UNKNOWN_OPERATOR():
    assert process_calculation("x", a, b) == ("ERROR", "", "UNKNOWN_OPERATION")
def test_INVALID_NUMBER():
    assert process_calculation("*", "r", b) == ("ERROR", "", "INVALID_NUMBER")
def test_DIVISION_BY_ZERO():
    assert process_calculation("/", a, c) == ("ERROR", "", "DIVISION_BY_ZERO")
def test_NO_ERROR():
    assert process_calculation("*", a, b) == ("OK", "20.0", "")