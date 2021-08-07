import sys
input = sys.stdin.readline
N, K = map(int, input().split())

left, right = 0, N // 2 + 1
while left < right:
    mid = left + (right - left) // 2
    cuts = (mid+1)*(N-mid+1)
    if cuts == K:
        print('YES')
        exit(0)
    elif cuts < K:
        left = mid + 1
    else:
        right = mid
print('NO')