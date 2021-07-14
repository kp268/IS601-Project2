from RNG.RandWithSeed import random_int, random_float


def random_ints(end, low, high):

    for i in end:
        rnglist = list(random_int(low, high))

    return rnglist


def random_floats(end, low, high):

    for i in end:
        rnglist = list(random_float(low, high))

    return rnglist
