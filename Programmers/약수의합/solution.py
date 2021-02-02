def solution(n):
    return sum(filter(lambda x:n%x==0, list(range(1,n+1))))
