import sys
input = sys.stdin.readline
N, D, K, C = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
coupon = set([C])
maxDishes = -1
for i in range(N):
    window = set([])
    if i + K <= N:
        window = set(sushi[i:i+K])
    else:
        window = set(sushi[i:] + sushi[:K - (N - i)])
    maxDishes = max(maxDishes, len(window | coupon))
print(maxDishes)