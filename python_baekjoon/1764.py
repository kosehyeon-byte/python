n, m = map(int, input().split())
nonheard = set(input() for _ in range(n))
nonseen = set(input() for _ in range(m))

nonheardandseen = sorted(nonheard & nonseen)
print(len(nonheardandseen))
for name in nonheardandseen:
    print(name)