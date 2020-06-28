from decimal import Decimal

from range_digit import RangeDigit


def test_it():
    d = RangeDigit("1.283")
    assert str(d) == "1.283"
    assert str(d / 2) == "0.641"
    d = RangeDigit("1.2830")
    assert str(d) == "1.2830"
    assert str(d / 2) == "0.6415"
    assert str(d + 1) == "2.2830"
    assert str(d - Decimal("0.3")) == "0.9830"
