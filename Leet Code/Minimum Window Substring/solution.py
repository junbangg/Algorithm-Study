# 실패 코드
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Dics and lists
        temp = count = collections.Counter(t)
        s = list(s)
        targets = []
        for i, v in enumerate(s):
            if v in t:
                targets.append(i)
        result = []
        maxlen = float('inf')
        window = collections.deque()
        keepTrack = []
        last = len(t)
        for ind, val in enumerate(targets):
            window.append(val)
            if s[val] not in keepTrack:
                temp[s[val]] -= 1
            keepTrack.append(s[val])                
            #check capacity of window
            print("first window :", window)
            if ind < last - 1:
                continue
            # from here on window is full
            candidate = s[window[0]:window[-1] + 1]
            print("candidate: ", candidate)
            if all(v == 0 for v in temp.values()) and len(candidate) <= maxlen:
                result = candidate
                maxlen= len(result)
            print(temp)
            print("window: ", window)
            print("result: ", result)                
            temp[s[window.popleft()]] += 1
        return ''.join(result)



