def whatType(obj):
    return type(obj)


def sameType(obj1, obj2):
    if isinstance(obj1, obj2):
        return True
    else:
        return False
