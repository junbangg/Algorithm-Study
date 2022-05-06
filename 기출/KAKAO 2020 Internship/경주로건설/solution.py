from collections import deque

def bfs(x, y, board):
    rowMax, colMax = len(board), len(board[0])
    distance = [[[float('inf')] * 4 for _ in range(colMax)] for _ in range(rowMax)]
    q = deque()
    q.append([x, y, 0, ""]) # x, y, cost, direction
    distance[x][y] = [0, 0, 0, 0]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # N S W E

    while q:
        x, y, cost, direction = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or nx >= rowMax or 0 > ny or ny >= colMax or board[nx][ny] == 1:
                continue
            newDirection = getDirection(i)
            nextCost = getCost(direction, newDirection) + cost
            if nextCost < distance[nx][ny][i]:
                distance[nx][ny][i] = nextCost
                q.append([nx, ny, nextCost, newDirection])
                
    return min(distance[rowMax-1][colMax-1])

def getCost(oldDirection, newDirection):
    return 100 if oldDirection == "" or oldDirection == newDirection else 600

def getDirection(index):
    directions = ['N', 'S', 'W', 'E']

    return directions[index]

def solution(board):
    return bfs(0, 0, board)
