def solution(numbers, target):
    N = len(numbers)
    answer = []
    def dfs(i, value):
        if i == N:
            if value == target:
                answer.append(value)
            return
        dfs(i+1, value + numbers[i])
        dfs(i+1, value - numbers[i])
    dfs(0, 0)
    return len(answer)
