n = int(input("Enter a number: "))
numlist = []
for _ in range(n):
    x, y = map(int, input("Enter two numbers separated by space: ").split())
    numlist.append((x, y))

numlist.sort(key=lambda x: (x[1], x[0]))
for num in numlist:
    print(num[0], num[1])