N = int(input())
nums = sorted([int(input()) for _ in range(N)], reverse = True)
answer = 0
for i in range(N):
    if (i+1) % 3 != 0:
        answer += nums[i]
print(answer)