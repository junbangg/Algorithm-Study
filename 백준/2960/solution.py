import sys
input = sys.stdin.readline

N, K = map(int, input().split())
sieve = [True] * (N+1)
cnt = 1
for i in range(2, N+1):
    if sieve[i]:
        for j in range(i, N+1, i):
            if sieve[j]:
                if cnt == K:
                    print(j)
                    exit(0)
                sieve[j] = False
                cnt += 1