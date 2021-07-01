from functools import cmp_to_key
import sys
N = int(sys.stdin.readline())
words = [sys.stdin.readline()[:-1] for _ in range(N)]

# if s1 > s2: return 1
def compare(s1, s2):
    n1, n2 = [], []
    zero1, zero2 = 0, 0
    for i in range(min(len(s1), len(s2))):
        a, b = s1[i], s2[i]
        # number
        if a.isnumeric() and not b.isnumeric():
            return 1
        if not a.isnumeric() and b.isnumeric():
            return -1
        if a.isnumeric() and b.isnumeric():
            if a == '0' and b == '0':
                zero1 += 1
                zero2 += 1
            if a == '0':
                return -1
            elif b == '0':
                return 1
            n1.append(a)
            n2.append(b)
        # letter
        else:
            if n1 and n2:
                if zero1 < zero2:
                    return 1
                if zero1 > zero2:
                    return -1
            n1, n2 = [], []
            zero1, zero2 = 0, 0




    pass

sortKey = cmp_to_key(compare)

words.sort(key = sortKey)



