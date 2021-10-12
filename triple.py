'''
Generates a random integer three times and returns the last one generated.

Params:
  generate: Function that generates the random integer.
  Params:
    a, b: Any two numbers.
  Returns:
    A random integer within the interval [a, b].
Returns:
  Nothing
'''

import functools
import random


def tripler(generate):
    @functools.wraps(generate)
    def one_value(one):
        @functools.wraps(one_value)
        def second_value(two):
            print(generate(one, two))
            return second_value
        return one_value
    return generate


@tripler
def generate(a, b):
    return random.randint(a, b)


print(tripler(generate(int(random.random() * 10), int(random.random() * 15))))
