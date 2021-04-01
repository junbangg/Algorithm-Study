def solution(n):
    nxt = n
    while True:
        nxt += 1
        if bin(nxt).count('1') == bin(n).count('1'):
            return nxt
