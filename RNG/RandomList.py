from RNG.RandWithSeed import random_int, random_float


def random_ints(n, low, high):

    for i in n:
        rnglist = list(random_int(low, high))

    return rnglist


def random_floats(n, low, high):

    for i in n:
        rnglist = list(random_float(low, high))

    return rnglist
