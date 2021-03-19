from collections import defaultdict
def solution(v):
    X = defaultdict(int)
    Y = defaultdict(int)
    for (x, y) in v:
        X[x] += 1
        Y[y] += 1
    return [min(X, key = X.get), min(Y, key = Y.get)]
