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
        if len(s) < 2 or s == s[::-1]: return s
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        longest = ""
        for i in range(len(s) - 1):
            longest = max(longest, expand(i, i+1), expand(i, i+2), key = len)
        return longest
