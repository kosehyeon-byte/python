n = int(input("Enter a number: "))
strset = set()
for _ in range(n):
    strset.add(input("Enter a string: ").rstrip())

strlist = list(strset)
strlist.sort(key=lambda x: (len(x), x))
for s in strlist:
    print(s)