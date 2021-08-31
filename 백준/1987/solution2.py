import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
    
# x, y, path, distance
q = set([(0, 0, board[0][0])])
answer = 1
while q:
    x, y, path = q.pop()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 > nx or nx >= N or 0 > ny or ny >= M:
            continue
        elif board[nx][ny] not in path:
            answer = max(answer, len(path + board[nx][ny]))
            q.add((nx, ny, path + board[nx][ny]))

print(answer)