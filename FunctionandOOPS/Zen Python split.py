print(type([2, 3]))
####iterator
x = [6, 3, 1]

s = iter(x)

print(next(s))  # -> 6

print(next(s))  # -> 3

print(next(s))  # -> 1

# print(next(s))      # -> StopIteration Error

# List Comprehension

x = [6, 3, 1]

y = [i ** 2 for i in x]  # List Comprehension expression

print(y)  # -> [36, 9, 1]

# Generator expression

x = [6, 3, 1]

g = (i ** 2 for i in x)  # generator expression

print(next(g))
print(next(g))
print(next(g))

# ************# *****

zenPython = '''

The Zen of Python, by Tim Peters



Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!

'''
import re

sentence = re.sub(r"\s+", "", zenPython, flags=re.UNICODE)

words = zenPython.split()
print(words)

print(len(words))
words = [a.strip('.--!* ') for a in words]
words = [a.lower() for a in words]
print(words)
print(len(words))

# word count and dictionary comprehension
word_frequency = {a: words.count(a) for a in words}

print(word_frequency)

# frequent words
frequent_words = {k: v for (k, v) in word_frequency.items() if v > 5}

print(frequent_words)

# Unique words

unique_words = set(words)

print(unique_words)


def fib_gen():
    n1 = 0
    n2 = 1
    count = 0
    while count < 100:
        yield n1
        n3 = n1 + n2
        n1 = n2
        n2 = n3


a = fib_gen()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


def factorial_gen(num):
    factorial = 1
    for i in range(1, num + 1):
        yield factorial
        factorial = factorial * i


b = factorial_gen(6)
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

dict1 = {0 if i % 2 == 0 else 1 for i in range(8)}
print(dict1)

dict2 = {ord(i) for i in 'apple'}
print(dict2)
