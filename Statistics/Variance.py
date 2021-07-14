from Statistics.Mean import findmean
from Calculator.Square import squarefunc
from Calculator.Division import divide


def findvariance(value):
    try:
        mean = findmean(value)
        deviation = [squarefunc(x - mean) for x in value]
        var = divide(sum(deviation) / len(value))

        return var

    except ValueError:
        print("List is empty")

    except ZeroDivisionError:
        print("Divide by 0 error")
