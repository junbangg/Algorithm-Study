import heapq
N = int(input())
nums = [int(input()) for _ in range(N)]
h = []
# create heap
for i in nums:
    heapq.heappush(h, i)
answer = 0
while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    answer += a+b
    heapq.heappush(h, a+b)
print(answer + heapq.heappop(h))