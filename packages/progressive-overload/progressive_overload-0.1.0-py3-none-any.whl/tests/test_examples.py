from pathlib import Path

import pytest
import yaml

from progressive_overload import progressive_overload


def load_examples():
    path = Path(__file__).parent / 'examples.yaml'
    with path.open() as file:
        return yaml.safe_load(file)


def parse_set(string):
    tokens = [token.strip() for token in string.split('x')]
    return float(tokens[0]), float(tokens[1])


def load_test_cases():
    examples = load_examples()

    test_cases = []

    for example in examples:
        progression = example['progression']
        max_reps = example['max_reps']
        weight_increment = example['weight_increment']

        pairs = list(zip([None] + progression, progression + [None]))[1:-1]

        for input, output in pairs:
            input = [parse_set(reps) for reps in input]
            output = [parse_set(reps) for reps in output]

            test_cases.append((input, output, max_reps, weight_increment))

    return test_cases


test_cases = load_test_cases()


@pytest.mark.parametrize("sets,expected,max_reps,weight_increment", test_cases)
def test_example(sets, expected, max_reps, weight_increment):
    assert progressive_overload(
        sets, max_reps=max_reps, weight_increment=weight_increment
    ) == expected
