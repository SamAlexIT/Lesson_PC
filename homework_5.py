"""homework_5"""


def row_arg():
    """row_arg"""
    arg_a = 'abcdefg hi jk lmn'
    print(arg_a)


def upper_arg():
    """upper_arg"""
    arg_a = 'abcdefg hi jk lmn'
    print(''.join(reversed(arg_a)))


def up_arg():
    """up_arg"""
    arg_a = 'abcdefg hi jk lmn'
    print(arg_a[:: -1])


def length_arg():
    """row_length_arg"""
    arg_a = 'abcdefg hi jk lmn'
    arg_b = len(arg_a)
    print(arg_b)


def list_length_arg():
    """list_length_arg"""
    arg_a = 'abcdefg hi jk lmn'
    arg_b = list(arg_a)
    print(arg_b)


def st_length_arg():
    """st_length_arg"""
    arg_a = 'abcdefg hi jk lmn'
    arg_b = list(arg_a[2:: 2])
    arg_c = '|'.join(arg_b)
    print(arg_c)
