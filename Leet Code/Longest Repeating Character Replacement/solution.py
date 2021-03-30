class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s = list(s)
        chances = k
        left, right, length = 0, 1, 1
        answer = []
        prev = s[left]
        while right < len(s):
            # 중복 문자일때
            if prev == s[right]:
                length += 1
                right += 1
            elif chances == 0:
                answer.append(length)
                chances = k
                left += 1
                right = left + 1
                length = 1
                prev = s[left]
            else:
                chances -= 1
                length += 1
                right += 1
        answer.append(length)            
        return max(answer)
    # Doesn't work because of ABBB
    # above code doesn't consider changing A to B

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
