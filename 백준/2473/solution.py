import sys
input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))
minVal = float('inf')
answer = [0, 0, 0]
for i in range(len(nums) - 2):

    left, right = i+1, len(nums) - 1
    
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if abs(minVal) > abs(total):
            answer = [nums[i], nums[left], nums[right]]
            minVal = total
        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            print(*answer)
            exit(0)
print(*answer)

