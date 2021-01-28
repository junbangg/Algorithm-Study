def solution(number, k):
    n = list(map(int, list(number)))
    big = sorted(list(n), reverse = True)[k-1]
    i, count = 0, 0
    while i < len(n) and count < k:
        if n[i] < big:
            n.pop(i)
            count += 1
            i = 0
        else:
            i += 1
    return ''.join(map(str,n))
