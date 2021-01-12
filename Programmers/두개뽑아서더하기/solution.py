def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                n = numbers[i] + numbers[j]
                if n not in answer:
                    answer.append(n)
    return sorted(answer)
