N = int(input())
nums = [[i, int(v)] for i, v in enumerate(input().split(), 1)]
i = 0
answer = []
while nums:
    ind, cur = nums.pop(i)
    answer.append(ind)
    if not nums:
        break
    if cur > 0:
        i = (i + cur - 1) % len(nums)
    else:
        i = (i + cur) % len(nums)
print(*answer)

