'''
#1 sort ads
#2 for each valid time frame, add candidate tasks to priority queue(max heap)
#3 if there is something in the queue, pop the next task and update (time, totalCost, count, last)
#4 do this until all ads are accounted for
'''
import heapq
def solution(ads):
    ads.sort()
    answer, last, time, count = 0, -1, 0, 0
    h = []
    while count < len(ads):
        for start, cost in ads:
            if last < start <= time:
                heapq.heappush(h, (-cost, start))
        if h:
            taskCost, startTime = heapq.heappop(h)
            last = time
            answer += (time - startTime) * -taskCost
            time += 5
            count += 1
        else:
            time += 1
    return answer




tc1 = [[1,3],[3,2],[5,4]] # 20
tc2 = [[0,3],[5,4]] # 0
tc3 = [[0,1], [0,2], [6,3], [8,4]]  # 40
tc4 = [[5,2], [2,2], [6,3], [9,2]] # 33

print(solution(tc1))
print(solution(tc2))
print(solution(tc3))
print(solution(tc4))
