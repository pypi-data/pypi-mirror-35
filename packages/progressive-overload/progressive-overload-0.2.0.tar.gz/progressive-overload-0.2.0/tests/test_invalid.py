import pytest

from progressive_overload import progressive_overload


def test_zero():
    sets = [(0, 10), (0, 10), (0, 10)]

    with pytest.raises(ValueError):
        progressive_overload(sets, max_reps=10, weight_increment=2.5)
