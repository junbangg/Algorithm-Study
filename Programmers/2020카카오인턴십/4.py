def solution(board):
    answers = []
    def dfs(x, y, lastDirection, cost):
        # out of bounds or '1'
        if x == len(board) -1 and y == len(board[0]) - 1:
            answers.append(cost)
            return
        elif x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == 1:
            return
        NSCost, WECost = 0, 0
        if lastDirection == 'N' or lastDirection == 'S':
            NSCost, WECost = 100, 600
        elif lastDirection == 'W' or lastDirection == 'E':
            NSCost, WECost = 600, 100
        else:
            NSCost, WECost = 100, 100
        #north
        if lastDirection != 'S':
            dfs(x-1, y, 'N', cost + NSCost)
        #south
        if lastDirection != 'N':
            dfs(x+1, y, 'S', cost + NSCost)
        #west
        if lastDirection != 'E':
            dfs(x, y+1, 'W', cost + WECost)
        #east
        if lastDirection != 'W':
            dfs(x, y-1, 'E', cost + WECost)
    dfs(0, 0, '', 0)
    return min(answers)
board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))

