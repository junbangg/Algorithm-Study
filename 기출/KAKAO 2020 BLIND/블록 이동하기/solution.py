from collections import deque
from typing import get_origin

def getRotationCoordinates(x, y):
    pass

def solution(board):
    dp = [[float('inf') for _ in range(len(board[0]))] for _ in range(len(board))]
    
    q = deque()
    q.append([0, 0, 0, 1])
    dp[0][0] = 0
    dp[0][0] = 0
    while q:
        x1, y1, x2, y2 = q.popleft()
        nextCoordinates = [(-1, 0), (1, 0), (0, -1), (1, 1)]
        nextCoordinates.extend(getRotationCoordinates(x1, y1))
        nextCoordinates.extend(getRotationCoordinates(x2, y2))

        for i in range(10):
            nx1, ny1, nx2, ny2 = x1, y1, x2, y2
            if i < 4: # NSWE
                # validate
                pass
            else: # Rotation
                # validate
                pass
            if (nx1, ny1, nx2, ny2) != (x1, y1, x2, y2):
                if 


    return 0