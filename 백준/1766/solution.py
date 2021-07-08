import heapq
N, M = list(map(int, input().split()))
pairs = [((list(map(int, input().split())))) for _ in range(M)]

dic = {}
h = []
#1 check list
#2 add to heap
#3 add to dic
check = [False for _ in range(N+1)]
for a, b in pairs:
    check[a] = True
    check[b] = True
    dic[a] = b
    heapq.heappush(h, a)

#add rest of numbers to heap
for i in range(1, N+1):
    if not check[i]:
        check[i] = True
        heapq.heappush(h, i)

# add to answer
answer = []
while h:
    num = heapq.heappop(h)
    answer.append(num)
    if num in dic:
        answer.append(dic[num])
print(*answer)
