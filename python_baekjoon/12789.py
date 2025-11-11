n = int(input())
line = list(map(int, input().split()))
line.reverse()
wait = []

for x in range(1, n + 1):
    if wait and wait[-1] == x:
        wait.pop()
    else:
        while line and line[-1] != x:
            wait.append(line.pop())
        if line and line[-1] == x:
            line.pop()
        else:
            print("Sad")
            break
else:
    print("Nice")


