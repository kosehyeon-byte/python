def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    num = int(input())
    candidate = num
    while True:
        if is_prime(candidate):
            print(candidate)
            break
        candidate += 1

'''
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
'''

'''
candidate = num
if candidate <= 2:
    print(2)
    continue
if candidate % 2 == 0:
    candidate += 1
while not is_prime(candidate):
    candidate += 2
print(candidate)
'''