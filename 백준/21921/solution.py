import sys
input = sys.stdin.readline
N, X = map(int, input().split())
nums = list(map(int, input().split()))

total = sum(nums[:X])
totals = [total]
left, right = 0, X
while right < N:
    total -= nums[left]
    total += nums[right]
    totals.append(total)
    left += 1
    right += 1

maxTotal = max(totals)
if maxTotal > 0:
    print(maxTotal)
    print(totals.count(maxTotal))
else:
    print("SAD")
