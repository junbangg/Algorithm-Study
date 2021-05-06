from collections import deque

def solution(board):
    # board lengths
    N = len(board)
    # changes in coordinates(x,y) for  North, South, West, East 
    directions = [[-1, 0, 'N'], [1, 0, 'S'], [0, -1, 'W'], [0, 1, 'E']]
    directionMap = {'N' : 0,
                    'S' : 0,
                    'W' : 1,
                    'E' : 1}
    # queue
    q = deque()
    # start and destination
    q.append([0,0,0,''])
    while q:
        cur_x, cur_y, curCost, curDir = q.popleft()
        for i in range(4):
            next_x = cur_x + directions[i][0]
            next_y = cur_y + directions[i][1]
            nextDir = directions[i][2]
            if 0 <= next_x < N and 0 <= next_y < N and board[next_x][next_y] != 1:
                nextCost = 100
                if curDir == '':
                    pass
                elif directionMap[nextDir] != directionMap[curDir]:
                    nextCost += 500
                 # check next data before adding to queue
                if board[next_x][next_y] == 0 or curCost + nextCost <= board[next_x][next_y]:
                    board[next_x][next_y] = curCost + nextCost
                    q.append([next_x, next_y, curCost + nextCost, nextDir])

    return board[N-1][N-1]
#board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
#board = [[0,0,0],[0,0,0],[0,0,0]]
#board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))


    
