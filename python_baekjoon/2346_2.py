from collections import deque
n = int(input())
balloons = deque()
values = list(map(int, input().split()))
for i in range(n):
    balloons.append((i + 1, values[i]))
result = []

while balloons:
    index, value = balloons.popleft()
    result.append(index)
    if not balloons:
        break
    if value > 0:
        balloons.rotate(-(value - 1))
    else:
        balloons.rotate(-value)

print(' '.join(map(str, result)))
