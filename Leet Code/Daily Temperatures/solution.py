def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, answer = [], [0] * len(T)
        for index, temp in enumerate(T):
            while stack and temp > T[stack[-1]]:
                old_index = stack.pop()
                answer[old_index] = index - old_index
            stack.append(index)
        return answer
