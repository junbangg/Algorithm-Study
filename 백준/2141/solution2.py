import sys
input = sys.stdin.readline
N = int(input())
nums = []
total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += b
    nums.append((a, b))
mid = total // 2
if total % 2 == 1:
    mid += 1
nums.sort(key = lambda x: x[0])
sum = 0
for a, b in nums:
    sum += b
    if sum >= mid:
        print(a)
        exit(0)
