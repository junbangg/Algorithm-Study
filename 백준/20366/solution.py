import sys
input = sys.stdin.readline
N = int(input())
snowballs = sorted(list(map(int, input().rstrip().split())))
answer = float('inf')
for i in range(N):
    for j in range(i+3, N):
        left, right = i+1, j-1
        while left <= right:
            _sum = (snowballs[i] + snowballs[j]) - (snowballs[left] + snowballs[right])
            answer = min(answer, abs(_sum))
            if _sum < 0:
                right -= 1
            else:
                left += 1
print(answer)


        
