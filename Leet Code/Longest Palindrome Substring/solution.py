class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(substring) > len(answer):
                    answer = substring
        return answer


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        longest = ""
        for i in range(len(s) - 1):
            longest = max(
                longest,
                expand(i, i+1),
                expand(i, i+2),
                key = len
            )
        return longest


# third attempt
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 2:
            if s == s[::-1]:
                return s
            else:
                return s[0]
        elif s == s[::-1]:
            return s
        answer = ""
        for i in range(1, len(s)):
            odd, even = "", ""
            a, b = -1, len(s)
            # odd lengthed version pal
            odd = s[i]
            c, d = i-1, i+1
            # even lengthed version pal
            if s[i-1] == s[i]:
                even = s[i-1:i+1]
                a, b = i-2, i+1
            while a >= 0 and b < len(s) and s[a] == s[b]:
                even = s[a] + even + s[b]
                a -= 1
                b += 1
            while c >= 0 and d < len(s) and s[c] == s[d]:
                odd = s[c] + odd + s[d]
                c -= 1
                d += 1
            pal = max(odd, even, key = lambda x: len(x))
            answer = max(answer, pal, key = lambda x: len(x))
        return answer
