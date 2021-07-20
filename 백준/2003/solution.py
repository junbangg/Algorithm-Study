import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

p1 = p2 = 0
total = nums[p1]
answer = 0
while 1:
    if total == M:
        answer += 1
        total -= nums[p1]
        p1 += 1
    elif total > M:
        total -= nums[p1]
        p1 += 1
    else:
        p2 += 1
        if p2 == N: break
        total += nums[p2]
print(answer)

# alternate solution

# N, M = map(int, input().split(' '))
# nums = list(map(int, input().split(' ')))
# answer = total = end = 0

# for start in range(N) :
#     while total < M and end < N :
#         total += nums[end]
#         end += 1
#     if total == M :
#         answer += 1
#     total -= nums[start]

# print(answer)