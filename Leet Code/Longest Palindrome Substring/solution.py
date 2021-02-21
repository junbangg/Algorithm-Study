class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(substring) > len(answer):
                    answer = substring
        return answer
