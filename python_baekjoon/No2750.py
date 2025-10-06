import sys

n = int(sys.stdin.readline())
numbers = []
for i in range(n):
    num = int(sys.stdin.readline())
    for j in range(len(numbers)):
        if num < numbers[j]:
            numbers.insert(j, num)
            break
    else:
        numbers.append(num)

for k in numbers:
    print(k)
