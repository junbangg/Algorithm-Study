from collections import deque
def solution(board):
    def getDirection(index):
        index_direction = {0: 'N', 1: 'S', 2: 'E', 3: 'W'}
        return index_direction[index]

    def getCost(direction1, direction2):
        sameDirections = {'N': ['N', 'S'], 'S': ['N', 'S'], 'E': ['E', 'W'], 'W': ['E', 'W']}
        isSameDirection = direction1 in sameDirections[direction2]

        return 100 if isSameDirection or direction1 == '' else 600

    def bfs(N):
        dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0] # N, S, E, W
        q = deque()
        q.append([0, 0, 0, '']) # x, y, cost, direction

        while q:
            x, y, cost, direction = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
                    nextDirection = getDirection(i)
                    nextCost = getCost(direction, nextDirection)
                    if board[nx][ny] == 0 or cost + nextCost <= board[nx][ny]:
                        board[nx][ny] = cost + nextCost
                        q.append([nx, ny, cost + nextCost, nextDirection])

    N = len(board)
    bfs(N)
    return board[N-1][N-1]

board = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]
# board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
print(solution(board))