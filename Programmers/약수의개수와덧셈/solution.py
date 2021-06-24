def check(num):
    amount = 0
    for i in range(1, num+1):
        if num % i == 0:
            amount += 1
    return amount

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if check(num) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer
