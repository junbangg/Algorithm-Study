from copy import deepcopy
from collections import deque

def bfs(board):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    X = Y = 5
    visited = [[0 for _ in range(X)] for _ in range(Y)]
    # distance = [[0 for _ in range(X)] for _ in range(Y)]
    startPositions = [] # (x, y)

    for x in range(X):
        for y in range(Y):
            if board[x][y] == 'P':
                startPositions.append((x, y))
    if not startPositions:
        return 1
    for src_x, src_y in startPositions:
        visited = deepcopy(visited)
        # distance = deepcopy(distance)
        visited[src_x][src_y] = 1
        q = deque()
        q.append([src_x, src_y, 1]) # x, y, distance 

        while q:
            x, y, distance = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 > nx or nx >= X or ny < 0 or ny >= Y or visited[nx][ny] or board[nx][ny] == 'X':
                    continue
                if board[nx][ny] == 'O':
                    visited[nx][ny] = 1
                    q.append([nx, ny, distance + 1])
                if board[nx][ny] == 'P' and distance <= 2:
                    print(visited)
                    return 0
        print(visited)
        return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer