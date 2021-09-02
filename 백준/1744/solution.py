import sys, collections
input = sys.stdin.readline

def solution(arr):
    answer = 0
    ones, neg, pos = 0, [], []
    for i in arr:
        if i == 1:
            ones += 1
        elif i > 1:
            pos.append(i)
        else:
            neg.append(i)
    neg.sort(reverse=True)
    pos.sort()
    while len(neg) >= 2:
        a = neg.pop()
        b = neg.pop()
        answer += a*b
    while len(pos) >= 2:
        a = pos.pop()
        b = pos.pop()
        answer += a * b
    if neg: answer += neg.pop()
    if pos: answer += pos.pop()
    return answer + ones

N = int(input())
nums = [int(input().rstrip()) for _ in range(N)]
print(solution(nums))