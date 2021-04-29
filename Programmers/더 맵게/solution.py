import heapq
def solution(scoville, K):
    scoville.sort()
    #split into two arrays
    prepare, finished = [], []
    for i, v in enumerate(scoville):
        if v < K:
            heapq.heappush(prepare, v)
        else:
            finished = scoville[i:]
            break
    answer = 0
    while prepare:
        if not finished and len(prepare) == 1:
            return -1
        a = heapq.heappop(prepare)
        if prepare:
            b = heapq.heappop(prepare)
        else:
            b = heapq.heappop(finished)
        new = a + 2*b
        if new >= K:
            heapq.heappush(finished, new)
        else:
            heapq.heappush(prepare, new)
        answer += 1
    return answer
