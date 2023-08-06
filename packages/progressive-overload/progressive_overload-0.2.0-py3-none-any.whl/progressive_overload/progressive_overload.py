"""Functions for calculating progressive overload sets."""

from decimal import Decimal
import itertools
import operator
import math


def apply_remainder(numbers, order, remainder, step, operator):
    indexes = itertools.cycle(order)

    i = next(indexes)
    while remainder > step:
        numbers[i] = operator(numbers[i], step)
        remainder -= step
        i = next(indexes)
    numbers[i] = operator(numbers[i], remainder)
    return numbers


def add_remainder(numbers, remainder, step):
    """
    Adds `remainder` to a list of values cyclically forwards incrementing by
    `increment` and then adds the rest.
    """

    return apply_remainder(
        numbers, range(len(numbers)), remainder, step, operator.add
    )


def subtract_remainder(numbers, remainder, step):
    """
    Subtracts `remainder` from a list of values cyclically backwards
    decrementing by `increment` and then subtracts the rest.
    """

    return apply_remainder(
        numbers, range(len(numbers) - 1, -1, -1), remainder, step, operator.sub
    )


def divide_evenly(a, b, step):
    """
    Divide a by b evenly returning a list of all the numbers. It works by
    distributing the remainder evenly across all elements in the list
    incrementing by `step`.
    """

    numbers = [a // b] * b
    remainder = a % b
    return add_remainder(numbers, remainder, step)


def calculate_new_weight_reps(current_weight, min_volume, max_no_reps, weight_increment):
    """
    Calculate the best weight x reps for a given minimum volume, the current
    weight across all sets, the maximum number of sets, and the weight
    increment.
    """

    weight = current_weight
    reps = math.ceil(min_volume / weight)

    while reps > max_no_reps:
        weight += weight_increment
        reps = math.ceil(min_volume / weight)

    return weight, reps


def calculate_new_sets(current_weight, min_volumes, max_reps, weight_increment):
    """
    Calculates the new sets given the current weight, the minumum volumes of
    each set, the maximum number of reps and the weight increment.
    """

    new_sets = []

    for i, min_volume in enumerate(min_volumes):
        weight, reps = calculate_new_weight_reps(
            current_weight, min_volume, max_reps, weight_increment
        )

        new_sets.append((weight, reps))

        remainder = reps * weight - min_volume

        if min_volumes[i + 1:]:
            min_volumes[i + 1:] = subtract_remainder(
                min_volumes[i + 1:], remainder, weight_increment
            )

    return new_sets


def progressive_overload(sets, *, max_reps: int, weight_increment: Decimal):
    """Find the next sets after progressively overloading."""

    current_volume = sum(set[0] * set[1] for set in sets)
    target_volume = current_volume + weight_increment

    current_weight = min(set[0] for set in sets)

    if current_weight <= 0:
        raise ValueError('Lowest weight is zero or less.')

    min_volumes = divide_evenly(target_volume, len(sets), weight_increment)

    return calculate_new_sets(
        current_weight, min_volumes, max_reps, weight_increment
    )
