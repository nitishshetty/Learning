import timeit


def f1():
    squares = []

    squares = [i ** 2 for i in range(1, 200000)]

    return (squares)


def f2():
    gen = (i ** 2 for i in range(1, 200000))

    return (gen)


print(timeit.timeit(f1, number=100))
print(timeit.timeit(f2, number=100))
