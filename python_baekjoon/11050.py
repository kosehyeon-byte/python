def two_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    return two_coefficient(n - 1, k - 1) + two_coefficient(n - 1, k)

n, k = map(int, input().split())
print(two_coefficient(n, k))