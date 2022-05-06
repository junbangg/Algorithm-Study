
def createPrefix(board, skills):
    for type, r1, c1, r2, c2, degree in skills:
        board[r1][c1] += degree if type == 2 else -degree
        board[r1][c2+1] += -degree if type == 2 else degree
        board[r2+1][c1] += -degree if type == 2 else degree
        board[r2+1][c2+1] += degree if type == 2 else -degree
    return board

def solution(board, skill):
    # padded board
    prefixBoard = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board)+1)]
    prefixBoard = createPrefix(prefixBoard, skill)

    rowCount, colCount = len(board), len(board[0])
    # row prefix
    for x in range(rowCount):
        for y in range(colCount):
            prefixBoard[x][y+1] += prefixBoard[x][y]
    # col prefix
    for x in range(rowCount):
        for y in range(colCount):
            prefixBoard[x+1][y] += prefixBoard[x][y]

    # get answer
    answer = 0
    for x in range(rowCount):
        for y in range(colCount):
            board[x][y] += prefixBoard[x][y]
            if board[x][y] >= 1:
                answer += 1
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))