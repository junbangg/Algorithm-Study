from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def checkCol(candidate, cur_col):
            if not candidate:
                return True
            cur_row = len(candidate)
            for prev_x, prev_y in enumerate(candidate):
                # same column
                if prev_y == cur_col or abs(prev_y - cur_col) == cur_row - prev_x:
                    return False
            return True
        
        def insertQueenAt(x, y, board):
            newBoard = deepcopy(board)
            newBoard[x] = newBoard[x][:y] + 'Q' + newBoard[x][y+1:]
            
            return newBoard
            

        def dfs(x, candidates, board, answers):
            if x == n:
                answers.append(board)
                return
            for y in range(n):
                # check if y is a valid place to place Queen
                if checkCol(candidates, y):
                    candidates.append(y)
                    newBoard = insertQueenAt(x, y, board)
                    dfs(x+1, candidates, newBoard, answers)
                    candidates.pop() # after dfs is done, no need to keep checking this collumn, so we pop and Prune

        answers = []
        board = ['.'*n for _ in range(n)]
        dfs(0, [], board, answers)
        
        return answers
