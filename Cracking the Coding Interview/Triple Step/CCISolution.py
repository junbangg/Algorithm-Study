# Book solution

def solution(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return solution(n-1) + solution(n-2) + solution(n-3)

print(solution(5))
