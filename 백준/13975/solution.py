import sys, heapq

input = sys.stdin.readline

def solution(files):
    answer = 0
    h = []
    for file in files:
        heapq.heappush(h, file)
    while len(h) > 1:
        num1 = heapq.heappop(h)
        num2 = heapq.heappop(h)
        _sum = num1 + num2
        answer += _sum
        heapq.heappush(h, _sum)
    return answer

T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    print(solution(files))

