import math

n = int(input())
tree = [int(input()) for _ in range(n)]
intervals = [tree[i+1] - tree[i] for i in range(n-1)]

gcdnum = intervals[0]
for i in range(1, len(intervals)):
    gcdnum = math.gcd(gcdnum, intervals[i])

result = sum((interval // gcdnum) - 1 for interval in intervals)
print(result)
