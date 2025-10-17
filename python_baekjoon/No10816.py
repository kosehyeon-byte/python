n = int(input())
numlist = list(map(int, input().split()))
m = int(input())
checklist = list(map(int, input().split()))

for i in checklist:
    print(numlist.count(i), end=' ')

'''
import sys
input = sys.stdin.readline

n = int(input())
numlist = list(map(int, input().split()))
m = int(input())
checklist = list(map(int, input().split()))

from collections import Counter
counter = Counter(numlist)

res = []
for x in checklist:
    res.append(str(counter.get(x, 0)))

print(" ".join(res))

'''

'''
import sys
import bisect
input = sys.stdin.readline

n = int(input())
numlist = sorted(map(int, input().split()))
m = int(input())
checklist = list(map(int, input().split()))

res = []
for x in checklist:
    left = bisect.bisect_left(numlist, x)
    right = bisect.bisect_right(numlist, x)
    res.append(str(right - left))

print(" ".join(res))

'''