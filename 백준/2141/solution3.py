import sys
input = sys.stdin.readline
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]
nums.sort(key = lambda x: x[0])
prefix = [nums[0][1]]
for i in range(1, N):
    prefix.append(prefix[-1] + nums[i][1])


left, right = 0, N-1
answer = float('inf')
while left <= right:
    mid = left + (right - left) // 2
    leftSum = prefix[mid]
    rightSum = prefix[-1] - prefix[mid]
    if leftSum >= rightSum:
        answer = min(nums[mid][0], answer)
        right = mid - 1
    else:
        left = mid + 1

print(answer)