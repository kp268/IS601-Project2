from collections import Counter


def findmode(value):
    try:
        count = Counter(value)
        getmode = dict(count)
        mode = [x for x, v in getmode.items() if v == max(list(count.values()))]
        getmode = mode[0]
        return getmode

    except ZeroDivisionError:
        print("Error: Divide by 0 is not acceptable")

    except ValueError:
        print("Error: list cannot empty")
