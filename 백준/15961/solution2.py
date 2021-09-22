import sys, collections
input = sys.stdin.readline
N, D, K, C = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
dic = collections.defaultdict(int)

coupon = False
# 첫 구간에 대한 딕셔너리 초기화
for r in range(K):
    dic[sushi[r]] += 1
    if sushi[r] == C:
        coupon = True

left, right = 0, r

currentDishes = maxDishes = len(dic)
# 첫 구간 안에 쿠폰 스시가 없으면 최대값에 1을 추가해준다
if not coupon:
    maxDishes += 1

while left < N - 1:
    # 슬라이딩 윈도우의 왼쪽으로 빠지는 스시 처리
    if dic[sushi[left]] == 1:
        if sushi[left] == C:
            coupon = False
        currentDishes -= 1
    dic[sushi[left]] -= 1
    left += 1
    
    # 슬라이딩 윈도우의 오른쪽으로 들어오는 새로운 스시 처리
    right += 1
    if dic[sushi[right % N]] == 0:   # 현재 슬라이딩 윈도우 안에 없을때(unique한 스시)
        if sushi[right % N] == C:
            coupon = True
        currentDishes += 1
    dic[sushi[right % N]] += 1

    # 쿠폰 사용(셰프가 새롭게 만들어주는 경우)
    if not coupon:
        maxDishes = max(maxDishes, currentDishes + 1)
    # 슬라이딩 윈도우 안에 이미 쿠폰스시가 있는 경우
    else:
        maxDishes = max(maxDishes, currentDishes)
    
print(maxDishes)