from collections import Counter

n = int(input())
nArray = list(map(int, input().split(' ')))
m = int(input())
mArray = list(map(int, input().split(' ')))

count = Counter(nArray)
for num in mArray:
    if count[num]:
        print('1')
    else:
        print('0')
