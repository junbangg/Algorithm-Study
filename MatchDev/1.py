import collections, heapq
def solution(t, r):
    answer = []
    # list for min heap
    h = []
    #dic for each person's [lift #, priority #]
    dic = collections.defaultdict(list)
    for i in range(len(t)):
        dic[t[i]].append([t[i], r[i]])
    # start algorithm
    last = max(dic.keys())
    for i in range(last + 1):
        # if new person arrives.. add to min heap
        if dic[i]:
            for data in dic[i]:
                heapq.heappush(h, (data[1], [data[0], i]))
        if h:
            item = heapq.heappop(h)
            answer.append([item[1][0], item[0]])
            #answer.append(heapq.heappop(h)[0])
        if h and i == last:
            while h:
                item = heapq.heappop(h)
                answer.append([item[1][0], item[0]])
    return answer

t = [7,7,8,1,1,0,0]
r = [3,2,3,2,1,1,0]
print(solution(t,r))
