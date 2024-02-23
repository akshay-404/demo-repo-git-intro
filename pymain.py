# Fibonacci Sequence
import numpy as np

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

seq = []
Nterms = int(input('Number of terms : '))
for i in range(Nterms):
    seq.append(fib(i))
print(seq)