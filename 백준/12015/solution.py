import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
dp = [0]

def binarySearch(arr, x):
    left, right = 1, len(dp) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid
        else:
            return mid
    return right

for n in nums:
    if dp[-1] < n:
        dp.append(n)
    else:
        dp[binarySearch(dp, n)] = n
print(len(dp)-1)
print(*dp[1:])