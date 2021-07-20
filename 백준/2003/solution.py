import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

answer = p1 = p2 = 0
total = nums[p1]
# while p1 <= p2 and p2 < N:
#     if total <= M:
#         if total == M:
#             answer += 1
#         p2 += 1
#         if p2 < N:
#             total += nums[p2]
#     else:
#         total -= nums[p1]
#         p1 += 1

N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
answer = total = end = 0

for start in range(N) :
    while total < M and end < N :
        total += nums[end]
        end += 1
    if total == M :
        answer += 1
    total -= nums[start]

print(answer)