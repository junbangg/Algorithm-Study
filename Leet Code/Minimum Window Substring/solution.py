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


# Accepted O(n) 풀이
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        # start, end 가 최소 윈도우 사이즈 기록
        left = start = end = 0
        for right, char in enumerate(s, 1):
            # 필요한거면 1 빼기
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            # 다 찾았으면 left 조절해서 윈도우 사이즈 줄이기
            if missing == 0:
                # need[s[left]] < 0 이라는 것은 우리가 찾는 단어가 아니라는 뜻
                # 그래서 left 가 우리가 찾는거 아닐 때마다 left로 윈도우를 좁힌다
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                # 지금 윈도우가 더 작으면 인덱스 저장 
                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]
