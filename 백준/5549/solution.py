import sys
input = sys.stdin.readline
N, M = map(int, input().split())
K = int(input())
_map = [[''] * (M+1)]
for _ in range(N):
    _map.append([''] + list(input().rstrip()))

# _map = [list(input().rstrip()) for _ in range(N)]

# 누적합
# J, O, I
prefix = [[[[0, 0, 0] for _ in range(M+1)] for _ in range(N+1)]]
print(prefix)
for i in range(1, N+1):
    for j in range(1, M+1):
        prefix[i-1][j] = prefix[i-1][j-1]
        if _map[i][j] == 'J':
            prefix[i-1][j][0] = prefix[i-1][j-1][0] + 1
        elif _map[i][j] == 'O':
            prefix[i-1][j][1] = prefix[i-1][j-1][1] + 1
        elif _map[i][j] == 'I':
            prefix[i-1][j][2] = prefix[i-1][j-1][2] + 1


# for _ in range(K):
#     a, b, c, d = map(int, input().split())
#     answers = [0, 0, 0]
#     for i in range(3):
#         answers[i] = prefix[c][d][i] - prefix[a-1][d][i] - prefix[c][b-1][i] + prefix[a-1][b-1][i]
#     print(*answers)

# 4 7
# 4
# JIOJOIJ
# IOJOIJO
# JOIJOOI
# OOJJIJO
# 3 5 4 7
# 2 2 3 6
# 2 2 2 2
# 1 1 4 7