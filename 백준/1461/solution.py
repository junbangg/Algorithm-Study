import sys
input = sys.stdin.readline

N, M = map(int, input().split())
negative, positive = [], []

for num in list(map(int, input().split())):
    if num < 0:
        negative.append(num)
    else:
        positive.append(num)

negative.sort(reverse=True)
positive.sort()
biggest = 0
if negative and positive:
    biggest = max(abs(negative[-1]), positive[-1])
else:
    if negative:
        biggest = abs(negative[-1])
    else:
        biggest = abs(positive[-1])

counter = answer = 0
while negative:
    if counter % M == 0:
        answer += abs(negative[-1] * 2)
    negative.pop()
    counter += 1
counter = 0
while positive:
    if counter % M == 0:
        answer += positive[-1] * 2
    positive.pop()
    counter += 1

print(answer - abs(biggest))

