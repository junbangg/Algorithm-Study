import sys
input = sys.stdin.readline
N, H = map(int, input().split())

up = [0] * (H + 1)
down = [0] * (H + 1)

# 짝수 홀수 구분해서 각 높이에 hit 수 추가
for i in range(N):
    if i % 2 == 0:
        up[int(input().rstrip())] += 1
    else:
        down[int(input().rstrip())] += 1

# 각 높이에 대한 hit 수 prefix sum 만들기
for i in range(H-1, 0, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

minHits = N
ways = 0
for i in range(1, H+1):
    if minHits > up[i] + down[H-i+1]:
        minHits = up[i] + down[H-i+1]
        ways = 1
    elif minHits == up[i] + down[H-i+1]:
        ways += 1
print(minHits, ways)