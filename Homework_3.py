def largest_number(arg_a, arg_b):

    a = int(input("Enter number: "))
    b = int(input("Enter number: "))

    print("largest_number")

    if a >= b:
        print(a)
    elif a <= b:
        print(b)
    else:
        print('largest_number')



def lesser_number(arg_a, arg_b, arg_c):

    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c = int(input("Enter number: "))

    print('lesser_number')

    if b >= a <= c:
        print(a)
    if a >= b <= c:
        print(b)
    if a >= c <= b:
        print(c)
    else:
        print("lesser_number")



def positive_number():

    a = int(input("Enter number: "))
    b = int(input("Enter number: "))

    print("positive_number")

    if a == (-a):
        print(abs(a))
    if b == (-b):
        print(abs(b))
    else:
        print("positive_number")



def sum_number():

    a = [5, 6, 2, 4]
    b = [3, 8, 1, 9]
    sum([a, b])

    print("sum_number")

    if a == [5, 6, 2, 4]:
         print(a)
    elif b == [3, 8, 1, 9]:
        print(b)
    else:
        print(sum([a, b]))



def number():

    a = int(input("Enter number: "))

    print("number")

    if a >= 0:
        print("positive")
    elif a <= -1:
        print("negative")
    else:
        print("number")