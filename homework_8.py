outside_var = 13
arr = []


def f():

    def g():
        # g()
        print(outside_var)

def use_arr():
    print(arr)
    #set_value_to_outside_var()


def set_value_to_outside_var():
    global outside_var  #, d, f
   # global outside_var
    outside_va = 17
    print(outside_va)


def modify_outside_var():
    global outside_var
    #outside_var = outside_var +10
    # global outside_var
    outside_va = 17
    print(outside_va)









a = 7


def pass_to_inner():
    a = outside_var + 10

    def inner():
        # global a
        nonlocal a
        a += 3
        print(a)

    print('before inner', a)
    inner()
    print('after inner', a)


if __name__=='__main':
    #use_outside_var()

    print('before', outside_var)
    #
    #
    pass_to_inner()
    print('after', outside_var)

    globals()

    print('before', arr)