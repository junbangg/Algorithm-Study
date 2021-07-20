import sys
input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = N+1
p1 = p2 = 0
total = nums[p1]
while 1:
    if total >= S:
        answer = min(answer, p2-p1+1)
        total -= nums[p1]
        p1 += 1
    else:
        p2 += 1
        if p2 == N: break
        total += nums[p2]
if answer == N+1:
    print(0)
else:
    print(answer)

