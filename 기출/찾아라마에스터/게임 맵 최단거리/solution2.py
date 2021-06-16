def solution(maps):

    answers = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, count):
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            answers.append(count)
            return
        maps[x][y] = 0
        for i in range(4):
            nextX, nextY = x + dx[i], y + dy[i]
            if nextX >= 0 and nextX < len(maps) and nextY >= 0 and nextY < len(maps[0]) and maps[nextX][nextY] == 1:
                dfs(nextX, nextY, count + 1)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                dfs(i, j, 1)
    return min(answers)


        
