# 1st
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
# 2nd
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        cur, change = prices[i], 0
        for j in range(i + 1, len(prices)):
            change += 1
            if prices[j] < cur:
                break
        answer[i] = change
    return answer
