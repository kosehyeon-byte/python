a, b = map(int, input().split())

result = [2**i for i in range(a, b + 1)]
result.pop(1)
result.pop(-2)
print(result)