import sys
input = sys.stdin.readline

# gcd(a,b) == gcd(b, a%b) stop when a%b == 0
def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a

N = int(input())
nums = list(map(int, input().split()))

# create prefix
LR, RL = [0] * N, [0] * N
LR[0] = nums[0]
RL[-1] = nums[-1]
for i in range(1, N):
    LR[i] = gcd(LR[i-1], nums[i])
for i in range(N-1, 0, -1):
    RL[i-1] = gcd(RL[i], nums[i-1])
answer, k = -1, 0
for i in range(N):
    res = 0
    if i == 0:
        res = RL[i+1]
    elif i == N-1:
        res = LR[i-1]
    else:
        res = gcd(LR[i-1], RL[i+1])
    if nums[i] % res != 0 and res > answer:
        answer = res
        k = nums[i]

if k == 0:
    print(answer)
else:
    print(answer, k, sep = ' ')


