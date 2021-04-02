from functools import reduce 
def solution(x):
    lst = list(str(x))
    sum = reduce(lambda a, b: a + b, map(int, lst))
    return x % sum == 0
