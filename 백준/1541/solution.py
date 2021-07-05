min_exp = input().split('-')
nums = []
for exp in min_exp:
    temp = exp.split('+')
    total = 0
    for t in temp:
        total += int(t)
    nums.append(total)
answer = nums[0]
for n in nums[1:]:
    answer -= n
print(answer)
