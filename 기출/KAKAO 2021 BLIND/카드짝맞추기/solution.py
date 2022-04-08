# 1. 모든 짝의 위치 저장
# 2. 카드 탐색 순서 조합으로 만들기
#   - 시작과 끝, 끝과 시작 둘다 탐색
# 3. 모든 조합에 대해서 bfs 실행해서 최솟값 찾기
from itertools import permutations
from collections import defaultdict
from collections import deque
import sys

def solution(board, r, c):
    def bfs(start, end):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        queue = deque()
        visited = [[0 for _ in range(4)] for _ in range(4)]
        queue.append([start[0], start[1], 1]) # x, y, moves
        visited[start[0]][start[1]] = 1
        
        shortestMoves = sys.maxsize

        while queue:
            x, y, moves = queue.popleft()

            # regular
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or visited[nx][ny]:
                    continue
                moves += 1
                if nx == end[0] and ny == end[1]:
                    shortestMoves = min(shortestMoves, moves + 1)
                    continue
                visited[nx][ny] = 1
                queue.append([nx, ny, moves])

            # ctr
            for i in range(4):
                ctrMoves = moves + 1
                nx, ny = x, y
                while nx < 4 and 0 <= nx and 0 <= ny and ny < 4 and board[nx][ny] == 0:
                    nx += dx[i]
                    ny += dy[i]
                
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or visited[nx][ny]:
                    continue
                ctrMoves += 1
                if nx == end[0] and ny == end[1]:
                    shortestMoves = min(shortestMoves, ctrMoves + 1)
                    continue
                visited[nx][ny] = 1
                queue.append([nx, ny, ctrMoves])
        return shortestMoves

    def search(index, current, start, end, perms, moves):
        global minMoves

        moves += bfs(current, start)
        board[current[0]][current[1]] = 0
        board[start[0]][start[1]] = 0
        moves += bfs(start, end)
        board[start[0]][start[1]] = 0
        board[end[0]][end[1]] = 0

        if index == len(perms) - 1:
            minMoves = min(minMoves, moves)
            return

        for i in range(index+1, len(perms)):
            first, second, = card_coordinates[perms[i]]
            search(i, end, first, second, perms, moves)
            search(i, end, second, first, perms, moves)

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
        global minMoves
        minMoves = sys.maxsize
        first, second = card_coordinates[perm[0]]
        search(0, current, first, second, perm, 0)
        search(0, current, second, first, perm, 0)
        answer = min(answer, minMoves)

    return answer