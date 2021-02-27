# 사이클 확인 too slow
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = collections.defaultdict(list)
        for a, b in prerequisites:
            course_map[a].append(b)
        traced = set()
        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            for x in course_map[i]:
                if not dfs(x):
                    return False
            traced.remove(i)
            return True
        for i in list(course_map):
            if not dfs(i):
                return False
        return True

# 가지치기 - 10 times faster
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = collections.defaultdict(list)
        for a, b in prerequisites:
            course_map[a].append(b)
        traced = set()
        visited = set()
        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True
            traced.add(i)
            for x in course_map[i]:
                if not dfs(x):
                    return False
            traced.remove(i)
            visited.add(i)
            return True
        for i in list(course_map):
            if not dfs(i):
                return False
        return True


