from collections import deque
from itertools import combinations

def solution(board):
    # find deletable
    def findDeletableBlocks(): # return [type, startX, startY, block]
        blocks = []
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] != 0:
                    block_path, block_directions = bfs(x, y, visited)
                    if isDeletable(block_directions):
                        blocks.append([board[x][y], x, y, block_directions, block_path])
        return blocks
                
    def isDeletable(block):
        if block in ["DRR", "DDL", "DDR", "DLL", "DLR"]:
            return True
        return False

    def isDeletableCoordinates(x, y):
        for row in range(x):
            if board[row][y] != 0:
                return False
        return True

    def getEmptyBlockCoordinates(block, x, y): #
        if block == "DRR":
            return [x, y + 1, x, y + 2]
        if block == "DDL":
            return [x, y - 1, x + 1, y - 1]
        if block == "DDR":
            return [x, y + 1, x + 1, y + 1]
        if block == "DLL":
            return [x, y - 1, x, y - 2]
        if block == "DLR":
            return [x, y - 1, x, y + 1]

    def bfs(src_x, src_y, visited):
        q = deque()
        q.append([src_x, src_y])
        visited[src_x][src_y]
        dx, dy = [0, 1, 0], [-1, 0, 1] # left, down, right
        index_direction = ["L", "D", "R"]
        type = board[src_x][src_y]
        path = [[src_x, src_y]]
        directions = ""
        counter = 0

        while q and counter < 3:
            x, y = q.popleft()
            for i in range(3):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not visited[nx][ny] and board[nx][ny] == type:
                    visited[nx][ny] = 1
                    counter += 1
                    directions += index_direction[i]
                    path.append([nx, ny])
                    q.append([nx, ny])
        return [path, directions]
    
    def deleteBlock(blockPath):
        for x, y in blockPath:
            board[x][y] = 0

    # generate combinations
    deletableBlocks = findDeletableBlocks()
    blockCombinations = combinations(deletableBlocks, len(deletableBlocks))

    answer = 0
    
    for combination in blockCombinations:
        deletedBlocks = 0
        for type, x, y, blockDirections, blockPath in combination:
            x1, y1, x2, y2 = getEmptyBlockCoordinates(blockDirections, x, y)
            if isDeletableCoordinates(x1, y1) and isDeletableCoordinates(x2, y2):
                deletedBlocks += 1
                deleteBlock(blockPath)
        answer = max(answer, deletedBlocks)
        
    return answer