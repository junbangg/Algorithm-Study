from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
temp = [list(map(int, input().split())) for _ in range(N)]
A,B,C,D = zip(*temp)
AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])

count = Counter(CD)
answer = 0
for num in AB:
    answer += count[-num]
print(answer)