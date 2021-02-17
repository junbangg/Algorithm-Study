
import itertools
N, M = map(int,input().split())
A = map(int, input().split())
maxnum = 0
for i in itertools.combinations(A, 3):
    if sum(i) < M and sum(i) >= maxnum:
        maxnum = sum(i)
print(maxnum)


