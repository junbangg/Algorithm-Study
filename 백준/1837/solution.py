import sys
input = sys.stdin.readline

def prime(n, k):
    sieve = [True] * (k)
    m = int(k ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:
            for j in range(i+i, k, i):
                sieve[j] = False
    return sieve

P, K = map(int, input().split())
sieve = prime(P, K)

flag = True 
for i in range(2, K):
    if sieve[i] and P % i == 0:
        flag = False
        break

if flag:
    print('GOOD')
else:
    print('BAD', i, sep = ' ')
        