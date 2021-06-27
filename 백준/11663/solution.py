import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
points = sorted(list(map(int, sys.stdin.readline().split())))

def binarySearch(start, end, left, right):
    l, r = left, right
    # start
    while l <= r:
        pivot = l + (r - l) // 2
        if points[pivot] < start:
            l = pivot + 1
        else:
            r = pivot - 1
    # save start index
    startIndex = l

    l, r = left, right
    # end
    while l <= r:
        pivot = l + (r - l) // 2
        if points[pivot] > end:
            r = pivot - 1
        else:
            l = pivot + 1
    endIndex = r + 1
    # return index range
    return endIndex - startIndex

for _ in range(M):
    low, high = map(int, sys.stdin.readline().split())
    left, right = 0, N - 1
    print(binarySearch(low, high, left, right))
