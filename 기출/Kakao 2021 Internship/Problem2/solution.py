import copy
def solution(places):
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    visitedOG = [[0 for _ in range(5)] for _ in range(5)]
   
    def dfs(x, y, grid, visited, dist):
        nonlocal safe
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            manhattan = abs(nx - x) + abs(ny - y)
            
            if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and dist + manhattan <= 2 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if grid[nx][ny] == 'O':
                    dfs(nx, ny, grid, visited, dist + manhattan)
                if grid[nx][ny] == 'P':
                    safe = False
                    return
         
    answer = []
    for place in places:
        P = []
        safe = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    P.append((i, j))
                    cnt = 0
        safe = True
        for x, y in P:
            visited = copy.deepcopy(visitedOG)
            visited[x][y] = 1
            dfs(x, y, place, visited, 0)
            if not safe:
                answer.append(0)
                break
        if safe: answer.append(1)
        
    return answer