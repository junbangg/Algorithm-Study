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

