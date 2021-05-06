from collections import deque
#maze = [[0,0,0],[0,0,0],[0,0,0]]
maze = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QueueNode:
    def __init__(self, point, cost, direct):
        self.point = point
        self.cost = cost 
        self.direct = direct

def isValid(x, y):
    if x >= len(maze) or x < 0 or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:
        return False
    return True

# North, South, West, East
directions = [[-1, 0, 'N'], [1, 0, 'S'], [0, -1, 'W'], [0, 1, 'E']]
directionMap = {'N': ['N', 'S'],
                'S': ['N', 'S'],
                'W': ['W', 'E'],
                'E': ['W', 'E']}
def bfs(source, dest):

    visited = [[False for i in range(len(maze[0]))]
               for j in range(len(maze))]
    print(visited)

    visited[source.x][source.y] = True
    q = deque()
    node = QueueNode(source, 0, "")
    q.append(node)

    while q:
        cur = q.popleft()
        pt = cur.point
        direct = cur.direct
        if pt.x == dest.x and pt.y == dest.y:
            return cur.cost
        # directions
        for i in range(4):
            next = directions[i]
            nextRow = pt.x + next[0]
            nextCol = pt.y + next[1]
            nextDir = next[2]
            nextCost = 0
            if direct == '':
                nextCost = 100
            elif direct in directionMap[nextDir]:
                nextCost = 100
            else:
                nextCost = 600
            if isValid(nextRow, nextCol) and not visited[nextRow][nextCol]:
                visited[nextRow][nextCol] = True
                adjNode = QueueNode(Point(nextRow, nextCol), cur.cost + nextCost, nextDir)
                q.append(adjNode)
start = Point(0,0)
end = Point(len(maze) - 1, len(maze[0]) - 1)
print(bfs(start, end))
