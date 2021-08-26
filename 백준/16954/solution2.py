import sys, collections
input = sys.stdin.readline
board = [list(input().rstrip()) for _ in range(8)]

#     0, E, W, N, S, NE, NW, SE, SW
dx = [0, 0, 0, -1, 1, -1, -1, 1, 1]
dy = [0, 1, -1, 0, 0, 1, -1, 1, -1]

def bfs(src_x, src_y):
    q = collections.deque()
    q.append((src_x, src_y))

    while q:
        # 벽이 이동한 후에, 다시 체크해줘야한다.
        visited = [[False] * 8 for _ in range(8)]
        for _ in range(len(q)):
            cur_x, cur_y = q.popleft()
            if cur_x == 0 and cur_y == 7:
                return 1

            if board[cur_x][cur_y] == '#':
                continue

            for i in range(9):
                nx, ny = cur_x + dx[i], cur_y + dy[i]
                if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

        # 행을 아래로 이동
        board.pop()
        board.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

    return 0

print(bfs(7, 0))