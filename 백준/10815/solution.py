from collections import Counter 
N = int(input())
has = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

counter = Counter(has)
answer = []
for i in check:
    if i in counter:
        answer.append(1)
    else:
        answer.append(0)
print(*answer)
