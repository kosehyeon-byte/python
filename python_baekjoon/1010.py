def combination(m,n):
    if n == 0 or n == m:
        return 1
    return combination(m - 1, n - 1) + combination(m - 1, n)

result = []

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result.append(combination(m, n))

print('\n'.join(map(str, result)))