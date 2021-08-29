def printBoard(board):
    for i in range(len(board)):
        print(*board[i])
    print('\n')

def pop(board, m, n):
    pop_set = set()
    # search squares
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i-1][j-1] == board[i-1][j] == board[i][j-1] != '_':
                pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
    # reset board
    for i, j in pop_set:
        board[i][j] = 0        
    for i, row in enumerate(board):
        empty = ['_'] * row.count(0)
        board[i] = empty + [block for block in row if block != 0]
    return len(pop_set)
     
def solution(m, n, board):
    answer = 0
    board = list(map(list,zip(*board)))
    printBoard(board)
    while True:
        res = pop(board, m, n)
        if res == 0: return answer
        answer += res