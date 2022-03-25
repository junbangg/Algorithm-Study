# 1. 모든 짝의 위치 저장
# 2. 카드 탐색 순서 조합으로 만들기
#   - 시작과 끝, 끝과 시작 둘다 탐색
# 3. 모든 조합에 대해서 bfs 실행해서 최솟값 찾기
from itertools import permutations
from collections import defaultdict
from collections import deque
import sys
from copy import deepcopy

def solution(board, r, c):
    def bfs(board, start, end):
        if start == end:
            return 0
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        queue = deque()
        visited = [[0 for _ in range(4)] for _ in range(4)]
        queue.append([start[0], start[1], 0]) # x, y, moves
        visited[start[0]][start[1]] = 1

        while queue:
            x, y, moves = queue.popleft()
            # regular
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                cx, cy = x, y
                while True:             # Ctrl + move
                    cx, cy = cx + dx[i], cy + dy[i]
                    if not (0 <= cx <= 3 and 0 <= cy <= 3):
                        cx, cy = cx - dx[i], cy - dy[i]
                        break
                    elif board[cx][cy] != 0:
                        break

                if nx == end[0] and ny == end[1] or cx == end[0] and cx == end[1]:
                    return moves + 1

                if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append([nx, ny, moves + 1])
                if not visited[cx][cy]:
                    visited[cx][cy] = 1
                    queue.append([cx, cy, moves + 1])

    def search(board, cursor, perm, moves):
        if len(perm) == 0:
            return moves
        card = perm[0]

        firstCard = card_coordinates[card][0]
        secondCard = card_coordinates[card][1]
        choice1Moves = bfs(board, cursor, firstCard) + bfs(board, firstCard, secondCard) + 2
        choice2Moves = bfs(board, cursor, secondCard) + bfs(board, secondCard, firstCard) + 2

        # change board
        nextBoard = deepcopy(board)
        nextBoard[firstCard[0]][firstCard[1]] = 0
        nextBoard[secondCard[0]][secondCard[1]] = 0

        if choice2Moves > choice1Moves: # choice1 이 최적
            return search(nextBoard, secondCard, perm[1:], moves + choice1Moves)
        else: # choice2가 최적
            return search(nextBoard, firstCard, perm[1:], moves + choice2Moves)

    cards = set()
    card_coordinates = defaultdict(list)

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] > 0:
                cards.add(board[x][y])
                card_coordinates[board[x][y]].append((x, y))
    
    # permutations
    perms = list(permutations(cards, len(cards)))
    
    answer = sys.maxsize
    current = [r, c]
    for perm in perms:
        minMoves = search(board, current, perm, 0)
        answer = min(answer, minMoves)

    return answer