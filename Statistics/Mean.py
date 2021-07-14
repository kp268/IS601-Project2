from Calculator.Addition import add
from Calculator.Division import divide

def mean(data):
    try:
        total = 0
        for x in data:
            total = add(x, total)
        return divide(total, len(data))

    except ValueError:
        print("List is empty")

    except ZeroDivisionError:
        print("Divide by 0 error")