from collections import deque
import heapq

def solution(n, camels):
    # edge case
    if n == 1:
        return camels[0]
    h, q = [], deque(sorted(camels))
    answer = 0
    while q:
        # pop from queue
        a = q.popleft()
        b = q.popleft()
        # add max camel to answer
        answer += max(a, b)
        # add to minheap
        heapq.heappush(h, a)
        heapq.heappush(h, b)
        # pop min from minheap and add back to queue
        goBack = heapq.heappop(h)
        if q:
            q.append(goBack)
            answer += goBack
    return answer

def main():
    N = int(input())
    for i in range(N):
        # input
        n = int(input())
        camels = list(map(int, input().split(' ')))
        # solution
        answer = solution(n, camels)
        # ouput
        print('#' + str(i + 1) + ' ' + str(answer))
        i += 1

main()
'''
n = 4
camels = [1, 2, 8, 9]
print(solution(n, camels ))
'''
