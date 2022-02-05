import sys
input = sys.stdin.readline

def solution(houses, N, M, K):
    currentSum = sum(houses[0:M])
    left = 1
    right = M
    answer = 1 if currentSum < K else 0
    # 예외처리
    if N == M:
        return answer

    while left < N:
        currentSum -= houses[left - 1]
        currentSum += houses[right % N]
        if currentSum < K:
            answer += 1
        left += 1
        right += 1
    return answer

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    houses = list(map(int, input().split()))
    print(solution(houses, N, M, K))
