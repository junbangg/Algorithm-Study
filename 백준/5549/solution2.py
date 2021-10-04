import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
_map = []
for i in range(n):
    _map.append(list(input()))
prefix = [[[0,0,0] for i in range(m+1)] for j in range(n+1)] 
# 2차원 prefix sum 문제에서는 행, 열이 한 줄씩 더 필요함!! 
for i in range(n):
    for j in range(m):
        for l in range(3):
            prefix[i+1][j+1][l] = prefix[i+1][j][l] +prefix[i][j+1][l]- prefix[i][j][l]
        if _map[i][j]=='J':
            prefix[i+1][j+1][0] += 1
        elif _map[i][j]=='O':
            prefix[i+1][j+1][1] +=1
        elif _map[i][j]=='I':
            prefix[i+1][j+1][2] += 1
for _ in range(k):
    a, b, c, d = map(int, input().split())
    answer = [0,0,0]
    for i in range(3):
        answer[i] = prefix[c][d][i]-prefix[a-1][d][i] - prefix[c][b-1][i] + prefix[a-1][b-1][i]
    print(answer[0], answer[1], answer[2])