from collections import deque

def solution(board):
    dp = [[float('inf') for _ in range(len(board[0]))] for _ in range(len(board))]
    print(dp)
    answer = 0
    return answer