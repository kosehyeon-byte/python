def stack_operations(operations):
    stack = []
    results = []
    
    for operation in operations:
        if len(operation) > 1:
            _, value = operation.split()
            stack.append(int(value))
        elif int(operation) == 2:
            if stack:
                results.append(stack.pop())
            else:
                results.append(-1)
        elif int(operation) == 3:
            results.append(len(stack))
        elif int(operation) == 4:
            results.append(1 if not stack else 0)
        elif int(operation) == 5:
            if stack:
                results.append(stack[-1])
            else:
                results.append(-1)
    
    return results

import sys

n = int(sys.stdin.readline())
operations = [sys.stdin.readline().strip() for _ in range(n)]
results = stack_operations(operations)

for result in results:
    print(result)