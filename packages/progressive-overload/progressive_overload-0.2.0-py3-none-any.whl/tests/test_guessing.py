from decimal import Decimal

import pytest

from progressive_overload import guess_max_reps, guess_weight_increment


@pytest.mark.parametrize("reps,max_reps", [
    ([], 12),
    ([10, 10, 10, 10, 10, 10, 12, 10, 10], 12),
    ([10, 10, 10, 11, 10, 10, 11, 11, 10, 11, 11, 11], 11),
])
def test_guess_max_reps(reps, max_reps):
    assert guess_max_reps(reps) == max_reps


@pytest.mark.parametrize("weights,increment", [
    ([], 2),
    ([10, 10, 10, 10, 10, 10, 10], 2),
    ([40, 40, 40, 45, 40, 40], 5),
    ([40, 40, 40, 42.5, 40, 40, 45, 42.5, 42.5], 2.5),
    ([10, 10, 8, 12, 10, 10], 2),
    ([9, 9, 9, 10, 9, 9, 11, 10, 9], 1),
])
def test_guess_weight_increment(weights, increment):
    decimal_weights = [Decimal(weight) for weight in weights]
    assert guess_weight_increment(decimal_weights) == Decimal(increment)
