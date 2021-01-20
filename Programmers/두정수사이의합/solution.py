import functools
def solution(a, b):
    if a > b: a,b = b, a
    return functools.reduce(lambda i,j : i+j, [x for x in range(a,b+1)])

#or

def solution(a, b):
    if a > b: a,b = b, a
    return sum(range(a, b+1))
