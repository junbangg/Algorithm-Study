from collections import defaultdict
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
dic = defaultdict(int)
for i in range(1, len(numbers)):
    numbers[i] += numbers[i-1]
    
for i in range(len(numbers)):
    if numbers[i] == k:
        answer += 1
    answer += dic[numbers[i]-k]
    dic[numbers[i]] += 1
print(answer)