import sys
input = sys.stdin.readline
T = int(input())
len_A = int(input())
A = list(map(int, input().split()))
len_B = int(input())
B = list(map(int, input().split()))

# 1 create sub arrays
subA, subB = [], []
for i in range(len_A):
    aTotal = A[i]
    subA.append(aTotal)
    for j in range(i+1, len_A):
        aTotal += A[j]
        subA.append(aTotal)
subA.sort()
for i in range(len_B):
    bTotal = B[i]
    subB.append(bTotal)
    for j in range(i+1, len_B):
        bTotal += B[j]
        subB.append(bTotal)
subB.sort(reverse=True)

# 2 Pointer
answer = p1 = p2 = 0
while p1 < len(subA) and p2 < len(subB):
    _sum = subA[p1] + subB[p2]
    if _sum == T:
        a_cnt, a_dup = 0, subA[p1]
        while p1 < len(subA) and subA[p1] == a_dup:
            a_cnt += 1
            p1 += 1
        b_cnt, b_dup = 0, subB[p2]
        while p2 < len(subB) and subB[p2] == b_dup:
            b_cnt += 1
            p2 += 1
        answer += a_cnt * b_cnt
    elif _sum < T:
        p1 += 1
    elif _sum > T:
        p2 += 1

print(answer)