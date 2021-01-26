def checkCount(c):
    if c == 1: return ''
    else: return str(c)

def solution(s):
    n, m = len(s), len(s)//2
    answer = [n]
    while m > 0:
        count = 1
        seq = ""
        prev = s[0:m]
        for i in range(m, n, m):
            temp = s[i:m+i]
            if temp == prev:
                count += 1
            else:
                seq += checkCount(count) + prev
                count = 1
                prev = temp
        seq += checkCount(count) + prev
        m -= 1
        if seq != "":answer.append(len(seq))
    return min(answer)
