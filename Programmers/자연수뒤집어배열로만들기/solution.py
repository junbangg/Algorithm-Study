# probably a better way to implement
def solution(n):
    return list(map(int, [i for i in str(n)]))[::-1]
