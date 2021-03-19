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
Accepted, but performance could be better
the Memory used is quite big as well
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return sqrt(x**2 + y**2)
        ogPoints = collections.defaultdict(list)
        dist = [distance(p[0], p[1]) for p in points]
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
