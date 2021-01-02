def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        current = prices[i]
        counter = 0
        for j in range(i+1, len(prices)):
            counter += 1
            if current > prices[j]:
                break
        answer.append(counter)
    return answer
