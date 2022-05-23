import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = input()

answer = []
counter = 0

for i in range(N):
    n = number[i]
    if answer and number[-1] < n and counter < K:
        answer.pop()
        counter += 1
    answer.append(n)
print(answer)
