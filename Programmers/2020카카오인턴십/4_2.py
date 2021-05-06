from collections import deque

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class DataNode:
    
    def __init__(self, point, cost, direction):
        self.point = point
        self.cost = cost
        self.direction = direction

def solution(board):
    # board lengths
    ROW, COL = len(board[0]), len(board)
    # changes in coordinates(x,y) for  North, South, West, East 
    directions = [[-1, 0, 'N'], [1, 0, 'S'], [0, -1, 'W'], [0, 1, 'E']]
    directionMap = {'N' : ['N', 'S'],
                    'S' : ['N', 'S'],
                    'W' : ['W', 'E'],
                    'E' : ['W', 'E']}

    def isValid(x, y):
        if x < 0 or x >= ROW or y < 0 or y >= COL or board[x][y] == 1:
            return False
        return True
    # queue
    q = deque()
    # visited map
    visited = [[False for i in range(ROW)] for j in range(COL)]
    # start and destination
    src, dest = Point(0, 0), Point(ROW-1, COL-1)
    start = DataNode(src, 0, "")
    q.append(start)
    while q:
        curNode = q.popleft()
        curPoint = curNode.point
        #current node data
        cur_x, cur_y = curPoint.x, curPoint.y
        curCost = curNode.cost
        curDir = curNode.direction
        # check if reached destination
        if cur_x == dest.x and cur_y == dest.y:
            return curCost 
        next_x, next_y, nextCost, nextDir = 0, 0, 0, ''
        for i in range(4):
            next_x = cur_x + directions[i][0]
            next_y = cur_y + directions[i][1]
            nextDir = directions[i][2]
            # Cost
            if curDir == '':
                nextCost = 100
            # Straight
            elif nextDir in directionMap[curDir]:
                nextCost = 100
            # Curve
            else:
                nextCost = 600
            # check next data before adding to queue
            if isValid(next_x, next_y) and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                nextNode = DataNode(Point(next_x, next_y), curCost + nextCost, nextDir)
                q.append(nextNode)


#board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
#board = [[0,0,0],[0,0,0],[0,0,0]]
#board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))


    
