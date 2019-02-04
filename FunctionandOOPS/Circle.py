class RadiusInputError(Exception):
    pass


class Circle:

    def __init__(self, radius):
        self.radius = radius
        if isinstance(self.radius, str):
            raise RadiusInputError()


try:
    if '2' == 2:
        a = Circle('Hello')

except RadiusInputError:
    print("'Hello' is not a number.")


class A:
    def __init__(self, x=5, y=4):
        self.x = x
        self.y = y

    def __str__(self):
        return 'A(x: {}, y: {})'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y


def f1():
    a = A(12, 3)
    b = A(3, 12)
    if (a == b):
        print(b != a)
        print(a)


f1()

print([i ** +1 for i in range(3)])


class class1:
    a = 1

    def f1(self):
        a = 2
        class1.a += 1
        print(class1.a, end=' ')
        print(a, end=' ')


class1().f1()
class1().f1()


class A:
    def __init__(self, a=5):
        self.a = a

        def f1(self):
            self.a += 10


class B(A):
    def __init__(self, b=0):
        A.__init__(self, 4)
        self.b = b

    def f1(self):
        self.b += 10


x = B()
x.f1()
print(x.a, '-', x.b)
