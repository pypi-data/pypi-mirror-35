# Progressive Overload

Calculates the next workout sets for progressive overload given previous
ones.

## Installing

```sh
$ pip install progressive-overload
```

## Using

```py
from progressive_overload import *

progressive_overload(
  [(8, 10), (8, 10), (8, 10)],  # weight x reps for each set
  max_reps=12,  # maximum number of reps per set in the output
  weight_increment=2,  # the amount the weight can increase by
)

guess_max_reps([12, 10, 10])  # the already performed reps

guess_weight_increment([Decimal(10), Decimal(8), Decimal(8)])  # the already performed weights
```

## Running

```sh
$ progressive-overload --max-reps 10 --increment 2 '8 x 10' '8 x 10' '8 x 10'
```

## Testing

```sh
$ pipenv install --dev
$ pipenv run python setup.py test
```
