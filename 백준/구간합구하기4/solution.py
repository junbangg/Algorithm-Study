#11659
import sys

n, m = list(map(int, sys.stdin.readline().split(' ')))
nums = list(map(int, sys.stdin.readline().split()))
prefix = [nums[0]]
for i in range(1, len(nums)):
    prefix.append(prefix[i-1] + nums[i])

for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split(' ')))
    if a >= 2:
        print(prefix[b-1] - prefix[a-2])
    else:
        print(prefix[b-1])