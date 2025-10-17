a = set(input().split())
b = set(input().split())
print(len(a.difference(b)) + len(b.difference(a)))