from decimal import Decimal
from typing import List


def guess_max_reps(reps: List[int], fallback: int = 12):
    """
    Guess the max reps for a list of performed rep counts.

    Calculated as the maximum value of the input reps.
    """

    if not reps:
        return fallback

    return max(reps)


def guess_weight_increment(weights: List[Decimal], fallback: Decimal = Decimal(2.0)):
    """
    Guess the weight increment given a list of performed weights. Expects the
    inputs to be `decimal.Decimal`s.

    Calculated by looking for commonly used weight demoninators.
    """

    unique_weights = set(weights)

    if len(unique_weights) <= 1:
        return fallback

    for multiple in [Decimal(5.0), Decimal(2.5), Decimal(2.0)]:
        if all(weight % multiple == 0 for weight in unique_weights):
            return multiple

    return Decimal(1.0)
