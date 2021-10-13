import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

answer = 0
left, right = 1, K
while left <= right:
    mid = left + (right - left) // 2
    temp = 0
    for i in range(1, N + 1):
        temp += min(mid//i, N)
    if temp >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)