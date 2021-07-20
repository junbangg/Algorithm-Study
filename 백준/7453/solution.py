import sys
input = sys.stdin.readline
N = int(input())

A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = [], []
for i in range(N):
    for j in range(N):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])
AB.sort()
CD.sort(reverse = True)
answer = p1 = p2 = 0
while p1 < len(AB) and p2 < len(CD):
    _sum = AB[p1] + CD[p2]
    if _sum == 0:
        # a_cnt, dup_a = 0, AB[p1]
        # while p1 < len(AB) and AB[p1] == dup_a:
        #     a_cnt += 1
        #     p1 += 1
        # b_cnt, dup_b = 0, CD[p2]
        # while p2 < len(CD) and CD[p2] == dup_b:
        #     b_cnt += 1
        #     p2 += 1
        # answer += a_cnt * b_cnt
        # p2-=1
        answer += 1
        p2 += 1
    elif _sum < 0:
        p1 += 1
    else:
        p2 += 1
print(answer)