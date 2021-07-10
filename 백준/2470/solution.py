N = int(input())
nums = sorted(list(map(int, input().split())))
start, end = 0, N-1
answer_start, answer_end = start, end
total = abs(nums[start] + nums[end])

while start < end:
    temp = nums[start] + nums[end]
    if abs(temp) < total:
        answer_start, answer_end = start, end
        total = abs(temp)
        if total == 0:
            break
    if temp > 0:
        end -= 1
    else:
        start += 1
print(nums[answer_start])
print(nums[answer_end])