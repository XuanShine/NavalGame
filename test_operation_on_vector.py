from operation_on_vector import getAngleDegFromVector


def test_getAngleDegFromVector():
    assert abs(getAngleDegFromVector((1, 0), (0, 1)) - 90) <= 0.01
    assert abs(getAngleDegFromVector((1, 0), (1, 1)) - 45) <= 0.01
    assert abs(getAngleDegFromVector((2, 2), (0, 3)) - 45) <= 0.01
    assert abs(getAngleDegFromVector((1, 0), (-1, 0)) - 180) <= 0.01
    assert abs(getAngleDegFromVector((1, 0), (-1, -1)) - 225) <= 0.01
    assert abs(getAngleDegFromVector((1, 0), (0, -1)) - 270) <= 0.01
    assert abs(getAngleDegFromVector((1, 0), (1, 0)) - 0) <= 0.01
    