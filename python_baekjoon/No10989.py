import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
count = [0] * 10001  # 값 범위: 1..10000

for _ in range(n):
    count[int(input())] += 1

for num in range(1, 10001):
    c = count[num]
    if c:
        # 같은 줄을 c번 곱해서 한 번에 출력 (빠르고 메모리도 안전)
        write((str(num) + '\n') * c)


