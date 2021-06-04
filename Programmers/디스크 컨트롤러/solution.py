import heapq
def solution(jobs):
    jobs.sort()
    count, last, time = 0, -1, 0
    total = 0
    h = []
    while count < len(jobs):
        for start, duration in jobs:
            if last < start <= time:
                heapq.heappush(h, (duration, start))
        if h:
            duration, start = heapq.heappop(h)
            last = time
            time += duration
            total += time - start
            count += 1
        else:
            time += 1
    return total // len(jobs)





jobs = [[0,3], [1,9], [2,6]]
#jobs = [[0,3], [1,8], [2,5]]
#jobs = [[0,5], [1,10], [2,8]]
#jobs = [[0,3], [5, 8], [4,3]]
print(solution(jobs))


