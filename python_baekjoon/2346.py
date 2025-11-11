n = int(input())
balloons = list(map(int, input().split()))
balloons = [(i+1, balloons[i]) for i in range(n)]
index = 0
result = []

while balloons:
    index %= len(balloons)
    result.append(balloons[index][0])
    value = balloons[index][1]
    balloons.pop(index)
    if not balloons:
        break
    if value > 0:
        index += value - 1
    else:
        index += value

print(' '.join(map(str, result)))