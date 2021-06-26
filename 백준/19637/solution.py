import sys
N, M = map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().split() for _ in range(N)]
'''
R = len(data) - 1
for _ in range(M):
    target = int(sys.stdin.readline())
    answer = 0
    left, right = 0, R
    while left <= right:
        pivot = left + (right - left) // 2
        if int(data[pivot][1]) >= target:
            answer = pivot
            right = pivot - 1
        else:
            left = pivot + 1
    print(data[answer][0])
'''
def binarySearch(target):
    answer = 0
    left, right = 0, len(data) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if int(data[pivot][1]) >= target:
            answer = pivot
            right = pivot - 1
        else:
            left = pivot + 1
    return answer

for _ in range(M):
    target = int(sys.stdin.readline())
    print(data[binarySearch(target)][0])
