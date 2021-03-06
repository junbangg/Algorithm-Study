# 최소 힙
from collections import Counter
import heapq
def solution(n, times):
    count, h = {}, []
    for t in times:
        count[t] = 0
    # 처음에는 다 심사 들어감 그냥
    answer = 0
    #n -= len(times)
    for key, val in count.items():
        heapq.heappush(h, (val + key, key,val))
    print(h)
    while n > 0:
        sum, key, time = heapq.heappop(h)
        print("N: {}, Time:{} Key:{} ".format(n, time, key))
        if time == 0:
            answer += time
        else:
            answer += time
            for i in range(len(h)):
                sum, val, key = h[i]
                if key - time <= 0:
                    h[i] = (key, key, 0)
                else:
                    h[i] = (sum - time, key, key - time)
        heapq.heappush(h, (key + key, key, key))
        n -= 1
        print(h)
        print(answer)
    return answer

# Binary Search
def solution(n, times):
    left, right = 1, max(times) * n
    answer = 0
    while left <= right:
        mid = left + (right - left) // 2
        people = 0
        for t in times:
            people += mid // t
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
