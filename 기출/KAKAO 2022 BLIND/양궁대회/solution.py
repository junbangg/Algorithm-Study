def getOptimal(arr1, arr2):
    isFirstArray = True
    for i in range(10, -1, -1):
        if arr1[i] > arr2[i]:
            return arr1
        if arr1[i] < arr2[i]:
            return arr2

def solution(n, info):    
    candidateArrows = []
    def dfs(index, arrows):
        if index == 11:
            _sum = sum(arrows)
            if _sum == n:
                candidateArrows.append(arrows)
            if _sum < n:
                arrows[-1] = n - _sum
                candidateArrows.append(arrows)
            return
        nextArrows = arrows[:]
        # win
        nextArrows[index] = info[index] + 1
        dfs(index+1, nextArrows)
        # missed
        dfs(index+1, arrows)

    arrows = [0] * 11
    dfs(0, arrows)
    maxScore = 0
    answer = []
    for candidate in candidateArrows:
        apeach = ryan = 0
        for i in range(11):
            if info[i] == candidate[i] == 0:
                continue
            if info[i] >= candidate[i]:
                apeach += 10 - i
            else:
                ryan += 10 - i
        if maxScore < ryan - apeach:
            maxScore = ryan - apeach
            answer = candidate
        elif answer and maxScore == ryan - apeach:
            answer = getOptimal(answer, candidate)
    if maxScore <= 0:
        return [-1]
    return answer
