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


def row_function_arg():
    """row_function_arg"""
    arg_a = 'abcdefg hi jk lmn'
    arg_b = list(arg_a[2:: 2])
    arg_c = '|'.join(arg_b)
    print(arg_c)

# метод sort() - сортування списку
# заданий список

A = [ 'a', 'f', 'v', 'd', 'n', 'b' ]

# сортування списку
A.sort()

B = [ 1, 3, 5, 10, 2, 8 ]
B.sort()

print("A = ", A)
print("B = ", B)

# метод count() - кількість входжень заданого елементу в списку
# заданий список
A = [ 'a', 'b', 'c', 'd', 'e', 'f' ]

na = A.count('d') # na = 1

B = [ 1, 3, 5, 3, 2, 4 ]
nb = B.count(3) # nb = 2

print("na = ", na)
print("nb = ", nb)

# метод sort() - сортування списку
# заданий список
C = [ 2, 3, 1, 5 ]
C.sort(reverse = True) # посортувати в порядку спадання
print("C = ", C)

# метод sort() - сортування списку з заданим ключем key
# заданий список рядків
S = [ "aBC", "ABCD", "ab", "ABCC", "DEFf" ]

S2 = list(S) # утворити новий список
S2.sort(key=str.upper) # посортувати з ключем key

S3 = list(S) # ще один список
S3.sort(key=str.upper, reverse=True) # посортувати з аргументами key та reverse

print("S = ", S)
print("S2 = ", S2)
print("S3 = ", S3)

# метод reverse() - реверсування списку
# задані списки
A = [ 1, 2, 3, 4, 5 ]
B = [ True, 7.78, 2.85, -1000, "bestprog.net" ]

# реверсування списків
A.reverse()
B.reverse()

print("A = ", A)
print("B = ", B)

# метод pop() - зменшення списку
# заданий список

A = [ 5, 3.8, True, False, "ABCD" ]

# видалити останній елемент
A.pop() # A = [5, 3.8, True, False]

print("A = ", A)

# видалити елемент з індексом 1
A.pop(1) # A = [5, True, False]

print("A = ", A)

# метод remove()
# заданий список
A = [ 5, 3.8, True, 3.8, True, False, "ABCD" ]

# видалити перший елемент, який рівний True
A.remove(True)

# видалити перший елемент, який рівний 3.8
A.remove(3.8)

print("A = ", A)