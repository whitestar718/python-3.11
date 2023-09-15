import os
import dis
import timeit

def add(a, b):
    return a + b

for i in range(10):
    add(3, 5)

dis.dis(add, adaptive=False)