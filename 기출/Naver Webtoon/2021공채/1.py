# 중복순열 + 슬라이딩 윈도우
from itertools import permutations

def solution(N, money, T, K):
    _range = []
    for i in range(N+1):
        _range += [i] * N
    candidates = set([perm for perm in permutations(_range, N) if sum(perm) == money])
    answer = 0
    testing = []
    for c in candidates:
        left, right = 0, T
        valid = True
        while right <= len(c):
            if sum(c[left:right]) > K:
                valid = False
                break
            left += 1
            right += 1
        if valid:
            answer += 1
            testing.append(c)
    print(testing)
    return answer
    

N = 4
money = 7
T = 2
K = 4

print(solution(N, money, T, K))