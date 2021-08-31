import sys, collections, copy
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip().lower()) for _ in range(N)]

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = collections.deque()
    visited = [0] * 26
    visited[ord(board[0][0]) - 97] = 1
    # x, y, visited_copy, distance
    # q.append((0, 0, copy.deepcopy(visited), 1))
    q.append((0, 0, visited[:], 1))
    answer = 0
    while q:
        x, y, visit, cnt = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visit[ord(board[nx][ny]) - 97] == 0:
                # nxt_visit = copy.deepcopy(visit)
                nxt_visit = visit[:]
                nxt_visit[ord(board[nx][ny]) - 97] = 1
                answer = max(answer, cnt + 1)
                q.append((nx, ny, nxt_visit, cnt+1))
    return answer


print(bfs())