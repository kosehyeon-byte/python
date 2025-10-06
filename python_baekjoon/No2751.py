import sys

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
numbers.sort()
print('\n'.join(map(str, numbers)))
