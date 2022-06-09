from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def isValidBoard(queens):
            for x in range(n):
                for y in range(n):
                    if queens[x][y] == 'Q':
                        for h in range(n):
                            if h == y: continue
                            if queens[x][h] == 'Q':
                                return False
                        for v in range(n):
                            if v == x: continue
                            if queens[v][y] == 'Q':
                                return False
            return True
                        
        nextPositions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        answer = []
        
        def dfs(x, y, queens, queenCount):
            if queenCount == n and isValidBoard(queens):
                answer.append(queens)
                return
            for i in range(x, n):
                for j in range(y, n):
                    for dx, dy in nextPositions:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and queens[nx][ny] != 'Q':
                            nextQueens = deepcopy(queens)
                            nextQueens[nx][ny] = 'Q'
                            dfs(nx, ny, nextQueens, queenCount+1)
                            # queens[nx][ny] = '.'
                
            
        startingQueens = [['.' for _ in range(n)] for _ in range(n)]
        dfs(0, 0, startingQueens, 0)
        
        return answer
        
