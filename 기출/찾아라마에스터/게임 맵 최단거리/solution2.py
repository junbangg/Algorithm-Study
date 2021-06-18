from collections import deque
def solution(maps):
    
    X, Y = len(maps), len(maps[0])
    def check(x, y, cost):
        if x >= 0 and x < X and y >= 0 and y < Y:
            if maps[x][y] == 1 or maps[x][y] > cost + 1:
                return True
        return False
    
    # N, S, W, E
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0, 1))
    while q:
        x, y, cost = q.popleft()
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            # check if valid
            if check(nextX, nextY, cost):
                maps[nextX][nextY] = cost + 1
                if nextX == X - 1 and nextY == Y - 1:
                    return maps[nextX][nextY]
                q.append((nextX, nextY, cost + 1))
    return -1