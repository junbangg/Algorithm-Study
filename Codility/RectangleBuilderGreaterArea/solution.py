from itertools import combinations_with_replacement
from collections import Counter

def solution(A, X):
    count = Counter(A)
    edges = combinations_with_replacement(list(set(A)), 2)
    answer = 0

    for x, y in edges:
        if x * y < X:
            continue
        if x == y:
            if count[x] >= 4:
                answer += 1
        elif count[x] >= 2 and count[y] >= 2:
            answer += 1
    return answer if answer <= 1000000000 else -1

