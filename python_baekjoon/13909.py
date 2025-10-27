import sys
input = sys.stdin.readline
n = int(input())

window = [0] * (n + 1)
for i in range(1,n+1):
    j=1
    while j*i <= n:
        window[j*i] = 1-window[j*i]
        j+=1

print(sum(window))

'''
import sys
from math import isqrt

n = int(sys.stdin.readline())
print(isqrt(n))   # floor(sqrt(n))

'''