def solution(board):
    row_max = len(board)
    col_max = len(board[0])
    def find_square(row, col, k):
        # base case
        if k == 1:
            return
        all_ones = True
        for i in range(row, row + k):
            for j in range(col, col + k):
                try: board[i][j]
                except: break
                if board[i][j] != 1:
                    all_ones = False
                    break
        if all_ones:
            answers.append(k*k)
        find_square(row, col, k-1)

    answers = [1]
    for i in range(row_max):
        for j in range(col_max):
            find_square(i, j , min(row_max, col_max))
    return max(answers)

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board2 = [[0,0,1,1],[1,1,1,1]]
board3 = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
board4 = [[0,0,0,0], [0,1,1,0], [0,1,1,0], [0,0,0,0]]
board5 = [[0,0,0,1]]
board6 = [[1,1], [1,1], [0,0], [0,0], [1,0]]
board7 = [[1, 0], [0,0]]
print(solution(board7))
