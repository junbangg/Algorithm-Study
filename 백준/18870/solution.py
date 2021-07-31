import sys, collections
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
dic = collections.defaultdict(int)
num_sorted = sorted(nums)
for i in range(1, N):
    if num_sorted[i] > num_sorted[i-1]:
        dic[num_sorted[i]] = dic[num_sorted[i-1]] + 1

print(*[dic[n] for n in nums])