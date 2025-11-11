s=list(map(int, input().split(';')))
s.sort(reverse=True)
for price in s:
    print(f'{price:>9,}')