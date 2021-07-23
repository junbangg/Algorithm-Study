import sys
input = sys.stdin.readline


def extendedGCD(a, b, K):
    s0, t0 = 1, 0
    s1, t1= 0, 1

    while b != 0:
        q = a // b
        r = a % b
        a, b = b, r

        s = s0 - q * s1
        t = t0 - q * t1
        s0, s1 = s1, s
        t0, t1 = t1, t
    t0 = (t0 % K + K) % K

    if a != 1 or t0 > 10 **9:
        return 'IMPOSSIBLE'
    return t0

t = int(input())
for i in range(t):
    K,C = map(int, input().split())
    if C == 1:
        if K+1 > 10**9:
            print('IMPOSSIBLE')
        else:
            print(K+1)
        continue
    if K == 1:
        print(1)
        continue
    answer = extendedGCD(K,C,K)
    print(answer)
        