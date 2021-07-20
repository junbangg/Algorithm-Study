from math import floor
import sys
input = sys.stdin.readline
X, Y = map(int, input().split())
Z = floor(100*Y/X)

if Z >= 99:
    print(-1)
else:
    left, right = 0, 1000000000
    while left<=right:
        mid = left + (right - left) // 2
        if Z < floor(100*(Y+mid)/(X+mid)):
            right = mid - 1
        else:
            left = mid + 1
    print(right+1)
