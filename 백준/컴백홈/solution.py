n, m, k = list(map(int, input().split(' ')))
map = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
start, end = [n-1, 0], [0, m-1]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y):
    if x == end[0] and y == end[1]:
        if visited[x][y] == k:
            return 1
        return 0
    dist = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or map[nx][ny] == 'T' or visited[nx][ny] != 0:
            continue
        visited[nx][ny] = visited[x][y] + 1
        dist += dfs(nx, ny)
        visited[nx][ny] = 0
    return dist
visited[start[0]][start[1]] = 1
print(dfs(start[0], start[1]))