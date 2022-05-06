import collections
x_move = [1,0,-1,0]
y_move = [0,1,0,-1]
MAX = 987654321
answer = MAX

def bfs(board):
    global answer
    # 최소비용을 기록하는 3차원 리스트 만듬. 처음엔 최댓값. [x축][y축][방향(밑,오른쪽,위,왼쪽 순서로)]
    visited = [[[MAX for y in range(len(board))] for x in range(len(board))] for z in range(4)]
    q = collections.deque()
    # [x, y, cost, dir]
    # dir -> 밑,오른쪽,위,왼쪽 -> 0,1,2,3
    # 0행0열 초기화
    for z in range(4):
        visited[z][0][0]= 0
    # 0행1열 초기화
    if board[0][1] != 1:
        q.append([0,1,100,1])
        visited[1][0][1] = 100
    # 1행0열 초기화
    if board[1][0] != 1:
        q.append([1,0,100,0])
        visited[0][1][0] = 100
    
    while q:
    	# x축, y축, 비용, 방향
        x, y, cost, dir = q.pop()
        
        for i in range(4):
        	# 다음에 이동할 x축 y축
            n_x = x + x_move[i]
            n_y = y + y_move[i]
            
            # 현재 방향과 다음에 이동할 방향이 틀리다면 +600원
            if dir != i:
                n_cost = cost + 600
            # 같다면 +100원
            else:
                n_cost = cost + 100
            
            #범위 안에 있고
            if 0 <= n_x < len(board) and 0 <= n_y < len(board):
                # 다음에 갈 곳이 벽도 아니며
                if board[n_x][n_y] != 1:
                	# 해당 [방향][x축][y축]에 기록되어있는 것보다 현재 비용이 작다면, 큐에 넣고 바꿔줌
                    if visited[i][n_x][n_y] > n_cost:
                        q.append([n_x, n_y, n_cost, i])
                        visited[i][n_x][n_y] = n_cost
    # x축y축 끝의 4방향 중에서 최솟값을 찾는다.
    for z in range(4):
        if answer > visited[z][len(board)-1][len(board)-1]:
            answer = visited[z][len(board)-1][len(board)-1] 
    return answer


def solution(board):
    return bfs(board)