import sys

input = sys.stdin.readline
t = int(input())

def sieve_flags(n: int) -> bytearray:
    if n < 1:
        return bytearray(n + 1)
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"  # 0,1 소수 아님
    limit = int(n ** 0.5)
    for p in range(2, limit + 1):
        if is_prime[p]:
            start = p * p
            step = p
            is_prime[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
    return is_prime

is_prime_flags = sieve_flags(1000000)

def count_goldbach_pairs(n: int) -> int:
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime_flags[i] and is_prime_flags[n - i]:
            count += 1
    return count

for _ in range(t):
    n = int(input())
    print(count_goldbach_pairs(n))

'''
import sys

def sieve_flags(n: int) -> bytearray:
    if n < 1:
        return bytearray(n + 1)
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0:2] = b"\x00\x00"
    limit = int(n ** 0.5)
    for p in range(2, limit + 1):
        if is_prime[p]:
            start = p * p
            step = p
            is_prime[start:n + 1:step] = b"\x00" * (((n - start) // step) + 1)
    return is_prime

MAXN = 1_000_000
is_prime_flags = sieve_flags(MAXN)

def count_goldbach_pairs(n: int) -> int:
    # (2, n-2) 한 쌍 먼저 처리
    cnt = 1 if is_prime_flags[2] and is_prime_flags[n - 2] else 0
    # i는 홀수만: 3,5,7,..., n//2
    half = n >> 1
    flags = is_prime_flags  # 로컬 바인딩으로 약간 빠름
    for i in range(3, half + 1, 2):
        if flags[i] and flags[n - i]:
            cnt += 1
    return cnt

input = sys.stdin.readline
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    out.append(str(count_goldbach_pairs(n)))
sys.stdout.write("\n".join(out))

'''