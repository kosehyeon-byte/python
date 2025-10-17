s = input()
partset = set()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        partset.add(s[i:j])
print(len(partset))