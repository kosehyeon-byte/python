# 0 - queue / fifo , 1 - stack / lifo
from collections import deque
n = int(input())
arr_input = list(map(int, input().split()))
arr = []
for i in arr_input:
    if i == 0:
        arr.append(deque())
    else:
        arr.append([])

value_input = list(map(int, input().split()))
for i in range(len(value_input)):
    arr[i].append(value_input[i])

test_deque = deque()
for stackqueue in arr:
    if isinstance(stackqueue, deque):
        test_deque.appendleft(stackqueue.popleft())


m = int(input())
test_values = list(map(int, input().split()))
result = []

for v in test_values:
    test_deque.append(v)
    result.append(test_deque.popleft())
    

print(' '.join(map(str, result)))