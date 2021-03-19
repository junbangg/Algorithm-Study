# insertion sort approach (too slow)
'''
Time Out
''''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def computeDistance(point):
            x, y = point[0], point[1]
            return sqrt(pow(x, 2) + pow(y, 2))
        i = 1
        while i < len(points):
            j = i
            while j > 0 and computeDistance(points[j-1]) > computeDistance(points[j]):
                points[j-1], points[j] = points[j], points[j-1]
                j -= 1
            i += 1
        return points[:k]

# Dictionary Approach
'''
Fastest
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ogPoints = collections.defaultdict(list)
        dist = [sqrt(x**2 + y**2) for (x,y) in points]
        for i, d in enumerate(dist):
            ogPoints[d].append(points[i])
        dist.sort()
        answers = [ogPoints[d] for d in dist[:k]]
        flat = []
        for a in answers:
            if len(a) == 1:
                flat.append(a[0])
            else:
                for p in a:
                    if p not in flat:
                        flat.append(p)
        return flat

# Min Heap solution
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p[0], p[1]
            distance = sqrt(x**2 + y**2)
            heapq.heappush(heap, (distance, [x, y]))
        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer

# Min Heap approach trimmed down
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p[0], p[1]
            distance = sqrt(x**2 + y**2)
            heapq.heappush(heap, (distance, [x, y]))
        return [heapq.heappop(heap)[1] for _ in range(k)]
