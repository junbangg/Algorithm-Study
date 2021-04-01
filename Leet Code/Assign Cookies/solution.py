# first solution
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        g.sort(reverse = True)
        s.sort(reverse = True)
        while g and s:
            if g[-1] <= s[-1]:
                g.pop()
                s.pop()
                answer += 1
            else:
                s.pop()
        return answer

# second solution
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child
# binary search solution
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
        return result
