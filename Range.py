a_range = range(5)
print('a_range ->', a_range)
print('list(a_range) ->', list(a_range))
# It is often used to execute a "for" loop a number of times
for i in range(5):
    print(i, end=' ')  # executed five times
print()
# it is similar to the slice function with a start, stop and step
a_range = range(10)
print('list(a_range) ->', list(a_range))
a_range = range(10, 16)  # start and stop
print('list(a_range) ->', list(a_range))
a_range = range(10, -1, -1)  # start , stop and step
print('list(a_range) -> ', list(a_range))


# ****************************
k1 = range(5)
print(list(k1))
k2 = range(10, 15)
print(list(k2))
k3 = range(10, 21, 2)
print(list(k3))
k4= range(100, 1, -25)
print(list(k4))

