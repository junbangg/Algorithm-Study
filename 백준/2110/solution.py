N, C = map(int, input().split())
points = sorted([int(input()) for _ in range(N)])
# edge case

def count(gap):
    prev, count = points[0], 1
    for i in range(1, len(points)):
        if points[i] - prev >= gap:
            count += 1
            prev = points[i]
    return count

def binarySearch(left, right):
    answer = 0
    while left <= right:
        gap = left + (right - left) // 2
        cnt = count(gap)
        if cnt >= C:
            left = gap + 1
            answer = gap
        else:
            right = gap - 1
    return answer


left, right = 1, points[-1] - points[0]
print(binarySearch(left, right))
