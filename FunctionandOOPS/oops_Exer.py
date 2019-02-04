import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return ('({},{},{})'.format(self.x, self.y, self.z))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)


def distance(point1, point2):
    d1 = math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2)
    return d1


p1 = Point(4, 2, 9)
p2 = Point(-2, -1, 4)
print(p1)
print(distance(p1, p2))
print(p1 + p2)

print(36 + '20')
