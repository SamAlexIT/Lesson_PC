""" homework """


def largest_number(arg_a, arg_b):
    """ largest_number """
    print("largest_number")

    if arg_a >= arg_b:
        return arg_a

    return arg_b


def lesser_number(arg_a, arg_b, arg_c):
    """ lesser_number """
    print('lesser_number')

    if arg_b >= arg_a <= arg_c:
        return arg_a
    if arg_b <= arg_c:
        return arg_b
    return arg_c


def positive_number(arg_a):
    """ positive_number """
    print("positive_number")

    if arg_a < 0:
        return -arg_a
    return arg_a


def sum_number(arg_a, arg_b):
    """ sum_number """
    print(arg_a + arg_b)


def number(arg_a):
    """ number """
    print("number")

    if arg_a > 0:
        print("positive")
    elif arg_a < 0:
        print("negative")
    else:
        print("zero")
