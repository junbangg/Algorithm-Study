from copy import deepcopy
import sys
sys.setrecursionlimit(10**7)

def solution(board, aloc, bloc):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    def isDefeated(x, y, board):
        # check if empty floor
        if board[x][y] == 0:
            return True
        # check surroundings
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny]:
                return False

        return True

    def dfs(board, turnPlayer, otherPlayer): # player = [A or B, x, y, moves]
        nonlocal aWinningMoves, bWinningMoves
        nonlocal aWinningDifference, bWinningDifference
        # nonlocal aWinning_aMoves, aWinning_bMoves, bWinning_aMoves, bWinning_bMoves
        # check if lose
        x, y = turnPlayer[1], turnPlayer[2]
        if isDefeated(x, y, board):
            winningDifference = abs(turnPlayer[3] - otherPlayer[3])
            if turnPlayer[0] == 'A': # A lost
                if winningDifference >= bWinningDifference:
                    bWinningDifference = winningDifference
                    bWinningMoves = min(bWinningMoves, turnPlayer[3] + otherPlayer[3])
            else: # B Lost
                if winningDifference >= aWinningDifference:
                    aWinningDifference = winningDifference
                    aWinningMoves = min(aWinningMoves, turnPlayer[3] + otherPlayer[3])
                # aWinningMoves = min(aWinningMoves, turnPlayer[3] + otherPlayer[3])
            # print(board)
            # print("-----loser-----:", turnPlayer[0])
            # print("loserMoves:", turnPlayer[3])
            # print("loser position", turnPlayer[1], turnPlayer[2])

            # print("winnerMoves:", otherPlayer[3])
            # print("winner position", otherPlayer[1], otherPlayer[2])
            # print("total:", turnPlayer[3] + otherPlayer[3])
            
            return
        hasToFollow = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 > nx or len(board) <= nx or 0 > ny or len(board[0]) <= ny or board[nx][ny] == 0:
                continue
            if nx == otherPlayer[1] and ny == otherPlayer[2]:
                continue
            hasToFollow = False
            newBoard = deepcopy(board)
            turnPlayerCopy = deepcopy(turnPlayer)
            turnPlayerCopy[1] = nx
            turnPlayerCopy[2] = ny
            turnPlayerCopy[3] += 1
            newBoard[x][y] = 0
            dfs(newBoard, otherPlayer, turnPlayerCopy)
        if hasToFollow:
            newBoard = deepcopy(board)
            turnPlayerCopy = deepcopy(turnPlayer)
            turnPlayerCopy[1] = otherPlayer[1]
            turnPlayerCopy[2] = otherPlayer[2]
            turnPlayerCopy[3] += 1
            newBoard[x][y] = 0
            dfs(newBoard, otherPlayer, turnPlayerCopy)
    
    aWinningDifference = bWinningDifference = 0
    aWinningMoves = bWinningMoves = float('inf')
    # aWinning_aMoves = float('inf')
    # aWinning_bMoves = 0
    # bWinning_aMoves = 0
    # bWinning_bMoves = float('inf')
    aPlayer = ['A', aloc[0], aloc[1], 0]
    bPlayer = ['B', bloc[0], bloc[1], 0]
    dfs(board, aPlayer, bPlayer)
    print(aWinningMoves)
    print(bWinningMoves)
    return aWinningMoves if aWinningDifference > bWinningDifference else bWinningMoves

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]

# board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# aloc = [1, 0]
# bloc = [1, 2]

# board = [[1, 1, 1, 1, 1]]
# aloc = [0, 0]
# bloc = [0, 4]


print(solution(board, aloc, bloc))