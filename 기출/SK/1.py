def solution(p):
    answer = [0] * len(p)
    for i in range(len(p)-1):
        minValue = min(p[i+1:])
        index = p.index(minValue)
        if p[i] > minValue:
            temp = p[i]
            p[i] = minValue
            p[index] = temp
            answer[i] += 1
            answer[index] += 1
    return answer