import sys
input = sys.stdin.readline
N = int(input())
temp = list(map(int, input().split()))

answer = [0 for _ in range(N)]
# recreate list -> (index, value)
nums = []
for i, v in enumerate(temp):
    nums.append((i, v))
# algorithm
stack = []
for i in range(N-1, -1, -1):
    ind, num = nums[i]
    if stack:
        while stack and stack[-1][1] <= num:
            key, val = stack.pop()
            answer[key] = ind+1
    stack.append((ind, num))
print(*answer)
