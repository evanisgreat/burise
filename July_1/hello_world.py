import timeit
from math import sqrt

def example():
    a = [x ** 2 for x in range(10001)]

print(timeit.timeit(example, number=1))
    