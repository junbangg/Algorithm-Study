def solution(n, lost, reserve):
    dup = set(reserve) & set(lost)
    reserve = set(reserve) - dup
    lost = set(lost) - dup
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r-1)
        elif r + 1 in lost:
            lost.remove(r+1)
    return n - len(lost)
