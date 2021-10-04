import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
_map = [list(input().rstrip()) for _ in range(N)]
# 누적합
# J, O, I
prefix = [[[0,0,0] for i in range(M+1)] for j in range(N+1)] 
for i in range(N):
    for j in range(M):
        for l in range(3):
            prefix[i+1][j+1][l] = prefix[i+1][j][l] + prefix[i][j+1][l] - prefix[i][j][l]
        if _map[i][j]=='J':
            prefix[i+1][j+1][0] += 1
        elif _map[i][j]=='O':
            prefix[i+1][j+1][1] +=1
        elif _map[i][j]=='I':
            prefix[i+1][j+1][2] += 1

for _ in range(K):
    a, b, c, d = map(int, input().split())
    answer = [0,0,0]
    for i in range(3):
        answer[i] = prefix[c][d][i]-prefix[a-1][d][i] - prefix[c][b-1][i] + prefix[a-1][b-1][i]
    print(answer[0], answer[1], answer[2])