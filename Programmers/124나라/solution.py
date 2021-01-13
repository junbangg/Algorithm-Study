def solution(n):
    nums = ['1', '2', '4']
    answer = ''

    while n > 0:
        n -= 1
        answer = nums[n%3] + answer
        n //= 3

    return answer

#or

def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]
