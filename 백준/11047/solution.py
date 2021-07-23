import sys
input = sys.stdin.readline

N, money = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)], reverse = True)
answer = 0
for c in coins:
    if c <= money:
        q, r = divmod(money, c)
        money = r
        answer += q
print(answer)


