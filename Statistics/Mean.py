from Calculator.Addition import add
from Calculator.Division import divide

def findmean(value):
    try:
        total = 0
        for x in value:
            total = add(x, total)
        return divide(total, len(value))

    except ValueError:
        print("List is empty")

    except ZeroDivisionError:
        print("Divide by 0 error")