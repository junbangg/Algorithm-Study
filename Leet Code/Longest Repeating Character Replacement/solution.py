# 2nd Try
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        left = right = 0
        start = end = 0
        count = collections.defaultdict(int)
        while left < len(s) and right < len(s):
            count[s[right]] += 1
            if (right - left + 1) - max(count.values()) <= k:
                if right - left + 1 > end - start + 1:
                    start, end = left, right
            else:
                count[s[left]] -= 1
                left += 1
            right += 1
        return end - start + 1
# Accepted Code
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        left = 0
        maxlen = 0
        for right in range(1, len(s) + 1):
            count[s[right - 1]] += 1
            max_char = count.most_common(1)[0][1]
            if right - left - max_char > k:
                count[s[left]] -= 1
                left += 1
            else:                
                maxlen = max(maxlen, right - left)
        return maxlen
