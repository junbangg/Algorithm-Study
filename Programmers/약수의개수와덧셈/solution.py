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



# different solution
# if number is square. divisor amount is odd
# because all divisors have a pair except squared numbers
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
