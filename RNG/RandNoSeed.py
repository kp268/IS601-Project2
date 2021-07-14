import random


def random_float(a, b):
    value = random.uniform(a, b)
    yield value


def random_int(a, b):
    value = random.randint(a, b)
    yield value
