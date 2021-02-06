import math
def solution(n):
    a = math.sqrt(n)
    return (a+1)**2 if a.is_integer() else -1
