import sys
N, S = map(int, input().split())
nums = list(map(int, input().split()))

def dfs(ind, total):
    global answer
    if total == S:
        answer += 1
    if ind >= len(nums):
        return
    for i in range(ind+1, len(nums)):
        dfs(i, total + nums[i])

answer = 0
for i in range(len(nums)):
    dfs(i, nums[i])
print(answer)