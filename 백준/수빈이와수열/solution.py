n, nums = int(input()), list(map(int, list(input().split(' '))))
total = 0
answer = []
for i, num in enumerate(nums):
    next = num*(i+1) - total
    answer.append(next)
    total += next
print(' '.join(map(str, answer)))