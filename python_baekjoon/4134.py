import math
import itertools

def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(2, n+1) if primes[i]]

n = int(input())

for i in range(n):
    num = int(input())
    
    primenums = sieve(num-1)
    for j in itertools.count(start=num):
        if all(j % p != 0 for p in primenums):
            print(j)
            break
