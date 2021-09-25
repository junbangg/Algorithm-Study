import sys, collections
input = sys.stdin.readline
N = int(input())
nums = sorted(list(map(int, input().split())))
dic = collections.Counter(nums)
answer = 0
for i in range(N):
    if dic[nums[i]] != 0:
        left, right = 0, N-1
        while left < right:
            if left == i:
                left += 1
                continue
            elif right == i:
                right -= 1
                continue
            if nums[i] == nums[left] + nums[right]:
                answer += dic[nums[i]]
                dic[nums[i]] = 0
                break
            elif nums[i] < nums[left] + nums[right]:
                right -= 1
            else:
                left += 1
print(answer)

# 7
# -4 -2 -2 -1 1 2 4

# 7
# -4 -2 -2 -2 -2 -2 2

# 7
# -3 -3 -1 0 2 3 5 