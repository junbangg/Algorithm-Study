def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def solution(n):
    answer = 0
    temp = ternary(n)
    for i in range(len(temp)):
        answer += int(temp[i]) * (3 ** i)
    return answer
