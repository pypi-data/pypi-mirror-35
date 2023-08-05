from argparse import ArgumentParser

from .progressive_overload import progressive_overload


def parse_set(string):
    tokens = [token.strip() for token in string.split('x')]
    return float(tokens[0]), float(tokens[1])


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-i', '--increment', type=float, default=2)
    parser.add_argument('-m', '--max-reps', type=int, default=12)
    parser.add_argument('sets', nargs='+', type=parse_set)
    return parser.parse_args()


def main():
    args = parse_args()

    new_sets = progressive_overload(
        args.sets, max_reps=args.max_reps, weight_increment=args.increment
    )

    for i, (weight, reps) in enumerate(new_sets):
        print(f'#{i + 1}\t{weight}', 'x', reps)
