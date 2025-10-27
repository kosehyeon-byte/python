import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

if b1 != b2:
    lcm = b1 * b2 // math.gcd(b1, b2)
    a1 *= lcm // b1
    a2 *= lcm // b2
    a1 += a2
    m = math.gcd(a1, lcm)
    print(a1 // m, lcm // m)
else:
    a1 += a2
    m = math.gcd(a1, b1)
    print(a1 // m, b1 // m)