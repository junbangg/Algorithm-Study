import sys
input = sys.stdin.readline

def binarySearch(arr, target):
    closest, closestCount = float('inf'), 0
    for i in range(len(arr)):
        left, right = i + 1, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            _sum = arr[i] + arr[mid]
            if abs(target - _sum) < closest:
                closest = abs(target - _sum)
                closestCount = 1
            elif abs(target - _sum) == closest:
                closestCount += 1
            if _sum > target:
                right = mid - 1
            else:
                left = mid + 1
    return closestCount
    
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    print(binarySearch(nums, k))

