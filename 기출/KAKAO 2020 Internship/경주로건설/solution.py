
def solution(board):
    def getDirection(index):
        index_direction = {0: 'N', 1: 'S', 2: 'E', 3: 'W'}
        return index_direction[index]

    def getCost(direction1, direction2):
        sameDirections = {'N': ['N', 'S'], 'S': ['N', 'S'], 'E': ['E', 'W'], 'W': ['E', 'W']}
        isSameDirection = direction1 in sameDirections[direction2]

        return 100 if isSameDirection or direction1 == '' else 600

    def dfs(x, y, cost, direction):
        nonlocal answer
        if x == N-1 and y == N-1:
            print(visited)
            answer = min(answer, cost)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            newDirection = getDirection(i)
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                newCost = getCost(direction, newDirection)
                dfs(nx, ny, cost + newCost, newDirection)
            visited[nx][ny] = False

    answer = float('inf')
    N = len(board)
    dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0] # N, S, E, W
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True

    dfs(0, 0, 0, '')
    return answer

board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
# board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
print(solution(board))