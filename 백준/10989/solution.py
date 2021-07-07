import sys
input = sys.stdin.readline
N = int(input())
nums = [0] * 10001
for _ in range(N):
    nums[int(input())] += 1
for i, v in enumerate(nums):
    if v != 0:
        for j in range(v):
            print(i)

