n = int(input("Enter a number: "))
numlist = list(map(int, input().split()))
numset = set(numlist)
packlist = []
count = 0
for num1 in numlist:
    for num2 in numset:
        if num2 < num1:
            count += 1
    packlist.append(count)
    count = 0

print(' '.join(map(str, packlist)))

'''
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# 중복 제거 + 정렬
sorted_unique = sorted(set(nums))

# 각 값의 압축된 인덱스를 딕셔너리에 저장
rank = {v: i for i, v in enumerate(sorted_unique)}

# 원래 순서대로 좌표 압축 결과 출력
print(' '.join(str(rank[x]) for x in nums))
'''