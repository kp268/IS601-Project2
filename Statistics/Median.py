from Calculator.Addition import add
from Calculator.Subtraction import subtract
from Calculator.Division import divide


# value is a list of numbers
def findmedian(value):
    # edge case
    if len(value) == 1:
        return value

    try:
        # costly but must be done
        value = value.sort()

        if len(value) % 2 == 0:

            median1 = value[len(value) // 2]
            median2 = value[len(value) // 2 - 1]
            median = (median1 + median2) / 2
        else:
            median = value[len(value) // 2]
        return median

    except ValueError:

        print("List is empty")

    except ZeroDivisionError:

        print("Divide by 0 error")
