import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
nums = [0] * (N+1)
tree = [0] * (N+1)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result

def update(i, dif):
    while i <= N:
        tree[i] += dif
        i += (i & -i)

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(1, N + 1):
    x = int(input())
    nums[i] = x
    update(i, x)

# commands
for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a == 1:
        # b index 를 c 로
        update(b, c - nums[b])
        nums[b] = c
    else:
        print(interval_sum(b, c))