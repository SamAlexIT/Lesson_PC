def infinite_loop():
    i = 0
    while True:
        yield i
        i += 1


def finite_loop():
    for i in range
    while True:
        yield i
        i += 1
def just_yield():
    yield 'abc'
    yield 'def'
    yield 13
    yield [1, 3]


  def manipulate(n):
      yield n
      n *= 2
      yield


if __name__ == '__main__':
    # l = [i for i in range(10)]
    g = (i for i in range(10))

    for i, el in enumerate(g):


    for i, el in enumerate(g):
        assert i + 5 == el

    for i, el in infinite_loop():
        print(el)
        if el == 10
            break

    g = finite_loop()
    while True:
        el = next(g, None)
        if

def another_yield():
    for el in just_yield():
        yield el


def another_yield_short():
    yield from just_yield()
    yield -1
    yield from(1, 2, 3)
    return 'abc'






    g = another_yield

    def password_checker(password):
        for real_pass_char, passed_pass_char in zip(PASSWORD, password):
            if real_pass_char != passed_pass_char:
                return

            time.sleep(0.1)

    def sum_of_list_items(arr):
        pass

    def cycle_words(words, output_length):
        pass

    def password_cracker():
        pass

    if __name__ == '__main__':
        assert sum_of_list_items([]) == 0
        assert sum_of_list_items([1, 2]) == 3
        assert sum_of_list_items([1, [2, 3, [4], [5, 6, [7]]]]) == 28

        assert cycle_words(['a', 'b', 'c'], 7) == ['a', 'b', 'c', 'a', 'b', 'c', 'a']
        assert cycle_words(['a', 'b', 'c'], 1) == ['a']
        assert cycle_words(['a', 'b', 'c'], 0) == []

        assert password_cracker() == PASSWORD

        

for i in range(5):
    print(i)


for j in range(15):
    print(j * 2)

for num in range(8):
    print("Привіт" * num)