import pytest
from app.shared.domain.value_object.point import Point

class TestPoint:

    def test_creates_valid_point(self):
        point = Point(10)
        assert point.value == 10

    def test_creates_zero_point(self):
        point = Point(0)
        assert point.value == 0

    def test_raises_on_negative_value(self):
        with pytest.raises(ValueError):
            Point(-1)

    def test_add_points(self):
        point1 = Point(10)
        point2 = Point(5)
        result = point1.add(point2)
        assert result.value == 15

    def test_subtract_points(self):
        point1 = Point(10)
        point2 = Point(5)
        result = point1.subtract(point2)
        assert result.value == 5

    def test_raises_on_insufficient_points(self):
        point1 = Point(5)
        point2 = Point(10)
        with pytest.raises(ValueError):
            point1.subtract(point2)

    def test_equality(self):
        assert Point(10) == Point(10)

    def test_inequality(self):
        assert Point(10) != Point(5)

    def test_immutable(self):
        from dataclasses import FrozenInstanceError
        point = Point(10)
        with pytest.raises(FrozenInstanceError):
            point.value = 20

    def test_add_returns_new_instance(self):
        point1 = Point(10)
        point2 = Point(5)
        result = point1.add(point2)
        assert result is not point1
        assert result is not point2

    def test_subtract_returns_new_instance(self):
        point1 = Point(10)
        point2 = Point(5)
        result = point1.subtract(point2)
        assert result is not point1
        assert result is not point2