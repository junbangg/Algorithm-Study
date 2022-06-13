# from collections import deque
# import heapq
# import sys
# def solution(grid, k):
#     dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
#     answer = sys.maxsize
#     visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
#     # q = deque()
#     q = []
#     visited[0][0] = True
#     # q.append([0, 0, 1, 0]) # x, y, chances, sleepCount
#     heapq.heappush(q, [0, 1, 0, 0]) # sleepcount,chances x, y,

#     while q:
#         sleepCount, chances, x, y = heapq.heappop(q)

#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if nx == len(grid) -1 and ny == len(grid[0]) - 1:
#                 answer = min(answer, sleepCount)
#                 break
#             if nx >= len(grid) or nx < 0 or ny >= len(grid[0]) or ny < 0 or visited[nx][ny] or grid[nx][ny] == '#':
#                 continue
#             visited[nx][ny] = True
#             if grid[nx][ny] == '.':
#                 heapq.heappush(q, [sleepCount + 1, 0, nx, ny])
#                 # q.append([sleepCount + 1, 0, nx, ny])
#             if chances < k:
#                 heapq.heappush(q, [sleepCount, chances+1, nx, ny])
#                 # q.appendleft([sleepCount, chances+1, nx, ny])
#     return answer
from collections import deque
import sys

def solution(grid, k):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    answer = sys.maxsize
    days = [[[False, sys.maxsize] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    q = deque()
    days[0][0] = 0
    q.append([0, 0, 1, 0]) # x, y, chances, sleepCount

    while q:
        x, y, chances, sleepCount = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx == len(grid) -1 and ny == len(grid[0]) - 1:
                answer = min(answer, sleepCount)
                break
            if nx >= len(grid) or nx < 0 or ny >= len(grid[0]) or ny < 0 or grid[nx][ny] == '#' or sleepCount > days[nx][ny]:
                continue
            days[nx][ny] = sleepCount
            if grid[nx][ny] == '.':
                q.append([nx, ny, 0, sleepCount + 1])
            if chances < k:
                q.append([nx, ny, chances+1, sleepCount])
    return answer
# grid = ["..FF", "###F", "###."]
grid = ["..", ".."]
print(solution(grid, 2))