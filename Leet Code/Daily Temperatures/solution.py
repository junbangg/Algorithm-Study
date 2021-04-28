# first attempt
def dailyTemperatures(self, T: List[int]) -> List[int]:
        dic = collections.defaultdict(collections.deque)
        stack, answer = [], [0] * len(T)
        for i, v in enumerate(T):
            dic[v].append(i)
        T = T[::-1]
        while T:
            temp = T.pop()
            index = dic[temp].popleft()
            while stack and stack[-1][0] < temp:
                startIndex = stack.pop()[1]
                answer[startIndex] = index - startIndex
            stack.append([temp, index])
        return answer
# trimmed down solution
def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, answer = [], [0] * len(T)
        for index, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                start = stack.pop()
                answer[start] = index -start 
            stack.append(index)
        return answer

