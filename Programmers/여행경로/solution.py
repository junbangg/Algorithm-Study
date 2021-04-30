import collections
import heapq
def solution(tickets):
    answer = []
    dic = collections.defaultdict(list)
    for a, b in tickets:
        heapq.heappush(dic[a], b)

    answer = []
    def dfs(city):
        while dic[city]:
            dfs(heapq.heappop(dic[city]))
        answer.append(city)
        
    dfs("ICN")
    return answer[::-1]
