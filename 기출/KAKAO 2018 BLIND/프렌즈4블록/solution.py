import collections


def printBoard(board):
    for i in range(len(board)):
        print(*board[i])
    print('\n')

def pop(m, n, board):
    count = 0
    delete = []
    for x in range(1, n):
        for y in range(1, m):
            if board[x][y] == board[x-1][y] == board[x-1][y-1] == board[x][y-1]:
                if (x, y) not in delete:
                    delete.append((x, y))
                if (x-1, y) not in delete:
                    delete.append((x-1, y))
                if (x-1, y-1) not in delete:
                    delete.append((x-1, y-1))
                if (x, y-1) not in delete:
                    delete.append((x, y-1))
    count += len(delete)
    minCol = [0] * n
    for x, y in delete:
        minCol[x] = min(minCol[x], y)
    for x, y in enumerate(minCol):
        board[x].
    return count

def solution(m, n, board):
    answer = 0
    board = list(map(list,zip(*board)))
    print(board)
    return answer
    # while True:
    #     pop = pop_num(b, m, n)
    #     if pop == 0: return answer
    #     answer += pop
    return answer

m, n = 6, 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))