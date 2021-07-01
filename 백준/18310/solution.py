N = int(input())
nums = sorted(list(map(int, input().split())))
print(nums[(len(nums)-1)//2])
