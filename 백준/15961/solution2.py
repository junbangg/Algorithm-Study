import sys, collections
input = sys.stdin.readline
N, D, K, C = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
dic = collections.defaultdict(int)

coupon = False
for r in range(K):
    dic[sushi[r]] += 1
    if sushi[r] == C:
        coupon = True
left, right = 0, r

currentDishes = maxDishes = len(dic)
if not coupon:
    maxDishes += 1

while left < N - 1:
    if dic[sushi[left]] == 1:
        if sushi[left] == C:
            coupon = False
        currentDishes -= 1
    dic[sushi[left]] -= 1
    left += 1
    
    right += 1
    if dic[sushi[right % N]] == 0:
        if sushi[right % N] == C:
            coupon = True
        currentDishes += 1
    dic[sushi[right % N]] += 1

    if not coupon:
        maxDishes = max(maxDishes, currentDishes + 1)
    else:
        maxDishes = max(maxDishes, currentDishes)
    
print(maxDishes)