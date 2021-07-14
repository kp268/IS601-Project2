import random


def random_float(a, b):
    random.seed(21398)

    value = random.uniform(a, b)
    yield value


def random_int(a, b):
    random.seed(12093)

    value = random.randint(a, b-1)
    yield value
