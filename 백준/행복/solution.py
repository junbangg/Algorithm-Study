n = int(input())
nums = list(map(int, list(input().split(' '))))
nums.sort()
print(nums[-1] - nums[0])