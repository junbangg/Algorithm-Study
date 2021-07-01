import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

dic = {}
for i in set(nums):
    dic[i] = 0

maxInterval = -sys.maxsize

left, right = 0, 0

while left <= right and right < N:
    cur = nums[right]
    if dic[cur] <= K-1:
        dic[cur] += 1
        maxInterval = max(maxInterval, right - left + 1)
        right += 1
    else:
        dic[nums[left]] -= 1
        left += 1
print(maxInterval)
