class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_map= collections.defaultdict(list)
        for fr, to in sorted(tickets):
            ticket_map[fr].append(to)
        def dfs(to):
            while ticket_map[to]:
                dfs(ticket_map[to].pop(0))
            route.append(to)
        route = []
        return route[::-1]
# optimized version
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_map = collections.defaultdict(list)
        for fo, to in sorted(list, reverse = True):
            ticket_map[fo].append(to)
        def dfs(to):
            while ticket_map[to]:
                dfs(ticket_map[to].pop())
            route.append(to)
        route = []
        dfs("JFK")
        return route[::-1]

# Using deque
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # set map
        dic = collections.defaultdict(collections.deque)
        for frm, to in sorted(tickets):
            dic[frm].append(to)
        result = []
        def dfs(dest):
            while dic[dest]:
                dfs(dic[dest].popleft())
            result.append(dest)
        dfs('JFK')
        return result[::-1]

# Iterative approach
class Solution:
    def findItinerary(self, tickets: List[List[str]]) - > List[str]:
        ticket_map = collections.defaultdict(list)
        for fo, to in sorted(tickets):
            ticket_map[fo].append(to)
        route, stack = [], ["JFK"]
        while stack:
            while stack[-1]:
                stack.append(ticket_map[stack[-1]].pop(0))
            route.append(stack.pop())
        return route[::-1]

