import sys, heapq
input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    heapq.heappush(h, int(input()))
answer = 0
while len(h) != 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    answer += a+b
    heapq.heappush(h, a+b)
print(answer)

# don't know why this didn't work

# import sys, heapq
# input = sys.stdin.readline

# h = []
# N = int(input())
# for _ in range(N):
#     heapq.heappush(h, int(input()))

# if len(h) == 1:
#     print(h[0])
#     exit(0)

# total = 0
# while len(h) >= 2:
#     a = heapq.heappop(h)
#     b = heapq.heappop(h)
#     total += a + b
#     if h:
#         heapq.heappush(h, a+b)
# print(total)