def solution(d, budget):
    d.sort()
    total, answer = 0, 0
    for i in d:
        total += i
        if total <= budget:
            answer += 1
    return answer

d, budget = [1,3,2,5,4], 9
print(solution(d, budget))


