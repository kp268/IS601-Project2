from Statistics.Variance import findvariance
from Calculator.SquareRoot import squarerootfunc


def findsd(value):

    try:
        variance = findvariance(value)
        return round(squarerootfunc(variance), 5)

    except ValueError:
        print("List is empty")

    except ZeroDivisionError:
        print("Divide by 0 error")