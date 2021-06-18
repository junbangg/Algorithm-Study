from collections import deque
def solution(maps):
    X, Y = len(maps), len(maps[0])
    visited = [[False for _ in range(X)] for _ in range(Y)]

    def check(x, y):
        if x >= 0 and x < X and y >= 0 and y < Y:
            if maps[x][y] == 1 and not visited[x][y]:
                return True
        return False
    
    # directions
    # N, S, W, E
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0, 1))
    while q:
        x, y, cost = q.popleft()
        visited[x][y] = True
        # add N, S, W, E to queue
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            # check if valid coordinates
            if check(nextX, nextY):
                if nextX == X - 1 and nextY == Y - 1:
                    return cost + 1
                q.append((nextX, nextY, cost + 1))
    return -1



maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
#maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))