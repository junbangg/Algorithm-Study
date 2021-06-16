from collections import deque
def solution(maps):
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    # directions
    # N, S, W, E
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, prev = q.popleft()
        print("{}, {} = {}".format(x, y, prev+1))
        if not visited[x][y]:
            visited[x][y] = True
            maps[x][y] += prev
        else:
            if maps[x][y] > prev + 1:
                maps[x][y] = prev + 1
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            if nextX < 0 or nextX >= 5 or nextY < 0 or nextY >= 5 or maps[nextX][nextY] == 0:
                continue
            elif not visited[nextX][nextY] or maps[nextX][nextY] > prev + 1:
                q.append((nextX, nextY, maps[x][y]))
    return -1 if maps[4][4] == 1 else maps[4][4]



maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
#maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))