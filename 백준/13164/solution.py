N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))
# base case
prefix = []
for i in range(1, N):
    prefix.append(nums[i] - nums[i-1])
print(sum(sorted(prefix)[:N-K]))