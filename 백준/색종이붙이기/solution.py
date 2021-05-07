from sys import stdin

# South, East, SouthEast
dx = [1, 0, 1]
dy = [0, 1, 1]
def dfs(x, y, xCount, yCount):
    for i in range(3):
        x += dx[i]
        y += dx[i]
        if matrix[x][y] != 1:
            pass
            # 지금까지 count 한걸로 판단
        else:
            if i < 2:
                xCount += 1
                yCount += 1
            dfs(x, y, xCount, yCount)
    return [xCount, yCount]





matrix = []
for _ in range(10):
    matrix.append([int(x) for x in stdin.readline().split()])
answer = 0
one, two, three, four, five = 5, 5, 5, 5,5

for i in range(10):
    for j in range(10):
        if matrix[i][j] == 1:
            dfs(i, j)


