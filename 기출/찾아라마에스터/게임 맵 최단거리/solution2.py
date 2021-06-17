from collections import deque
def solution(maps):
    X, Y = len(maps), len(maps[0])
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    # N, S, W, E
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, prev = q.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            maps[x][y] += prev
        else:
            if maps[x][y] > prev + 1:
                maps[x][y] = prev + 1
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            if nextX < 0 or nextX >= X or nextY < 0 or nextY >= Y or maps[nextX][nextY] == 0:
                continue
            elif not visited[nextX][nextY] or maps[nextX][nextY] > prev + 1:
                q.append((nextX, nextY, maps[x][y]))
    return -1 if maps[X-1][Y-1] == 1 else maps[X-1][Y-1]


        
