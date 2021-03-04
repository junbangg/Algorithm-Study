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
