def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        maxlen, start = 0, 0
        for index, value in enumerate(s):
            if value in dic and start <= dic[value]:
                start = dic[value] + 1
            else:
                maxlen = max(maxlen, index - start + 1)
            dic[value] = index
        return maxlen


# 2nd Attempt
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        stack = []
        for c in s:
            if c in stack:
                index = stack.index(c)
                # Reset Stack by removing characters before duplicate
                stack = stack[index + 1:]
            stack.append(c)
            maxlen = max(maxlen, len(stack))
        return maxlen
