grid = [
    ['1', '1', '1', '1', '0', '0'],
    ['0', '0', '1', '0', '1', '0'],
    ['0', '0', '1', '0', '1', '0'],
    ['0', '0', '1', '1', '1', '0'],
    ['0', '0', '0', '0', '1', '1']
]

def solution(r, c):
    def DFS(i, j, s):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] == '0':
            return
        path.append(s)
        grid[i][j] = '0'
        DFS(i, j+1, 'R')
        DFS(i+1, j, 'D')
    path = []
    DFS(0, 0, '')
    return path


print(solution(len(grid), len(grid[0])))
