from collections import defaultdict
def solution(X, A):
    leaves = defaultdict(int)
    needs = X
    for second, leaf in enumerate(A):
        if leaves[leaf] == 0:
            leaves[leaf] += 1
            needs -= 1
        # if all leaves have fallen 
        if needs == 0:
            return second
    return -1
