import sys
input = sys.stdin.readline

n = int(input())
stack = []
out = []

for _ in range(n):
    parts = input().split()
    op = int(parts[0])

    if op == 1:
        stack.append(int(parts[1]))
    elif op == 2:
        out.append(str(stack.pop() if stack else -1))
    elif op == 3:
        out.append(str(len(stack)))
    elif op == 4:
        out.append('1' if not stack else '0')
    elif op == 5:
        out.append(str(stack[-1] if stack else -1))

print('\n'.join(out))
