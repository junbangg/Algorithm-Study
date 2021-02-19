# first try
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)):
            s.insert(0, s.pop(i))
# optimized second try
class Solution:
    def reverseString(self, s: List[str]) -> None:
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            temp = s[p1]
            s[p1] = s[p2]
            s[p2] = temp
            p1 += 1
            p2 -= 1


# 책 solution .. 내거 두 번쨰가 더 빠름
class Solution:
    def reverseString(self, s: List[str]) -> None:
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1

# 책 solution  가장빠름
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        #안됨
        #s = s[::-1]
        # 됨
        s[:] = s[::-1]

