# my solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]
        if not chars: return True
        return chars == chars[::-1]

# 책 solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]
        if not chars: return True
        while len(chars) > 1:
            if chars.pop(0) != chars.pop():
                return False
        return True

# 책 solution 2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for c in s:
            if c.isalnum(): strs.append(c.lower())
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True



