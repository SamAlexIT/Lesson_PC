"""homework_4"""


def positional_arguments(*arg_a):
    """positional_arguments"""
    return list(set(arg_a))


def naming_arguments(**arg_1):
    """naming_argument"""
    print(arg_1['a'])
    print(len(arg_1))
    print(arg_1.get('user_type', 'Student'))


naming_arguments(a=8, b=3, c=6, d=7, user_type='abc')
naming_arguments(a=8, b=3, c=6, d=7)


# def named_arguments(arg_a, arg_b, /, arg_c, *, arg_d, arg_i=3, arg_f=4):
#    """named_arguments"""
#
def product_info(arg_a):
    """product_info"""
    def inner_function(arg_b):
        return arg_b * arg_a
    return inner_function


# inner_function = product_info(15)
# print(inner_function(5))
def size_m(arg_a):
    """size_m"""
    arg_m = arg_a
    for i in range(0, arg_a):
        for i in range(0, arg_m):
            print(end="")
        arg_m = arg_a
        for i in range(0, arg_a):

            print("*", end='')
        print("")
