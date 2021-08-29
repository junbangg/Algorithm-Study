def printBoard(board):
    for i in range(len(board)):
        print(*board[i])
    print('\n')

def pop(m, n, board):
    delete = set()
    for x in range(1, n):
        for y in range(1, m):
            if board[x][y] == board[x-1][y-1] == board[x-1][y] == board[x][y-1] != '_':
                delete |= set([(x, y), (x-1, y-1), (x-1, y), (x, y-1)])

    for x, y in delete:
        board[x][y] = 0

    for i in range(len(board)):
        empty = ['_'] * board[i].count(0)
        board[i] = empty + [c for c in board[i] if c != 0]

    return len(delete)

def solution(m, n, board):
    answer = 0
    board = list(map(list,zip(*board)))
    while True:
        res = pop(m, n, board)
        if res == 0: return answer
        answer += res

m, n = 6, 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))