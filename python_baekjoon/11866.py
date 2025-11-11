n, k = map(int, input().split())
round = list(i for i in range(1, n + 1))
ans = []
idx = 0

for i in range(n):
    idx = (idx + k - 1) % len(round)
    ans.append(round.pop(idx))

print("<" + ", ".join(map(str, ans)) + ">")