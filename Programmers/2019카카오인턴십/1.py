import collections
def solution(board, moves):
    answer = 0
    # change to dic
    dic = collections.defaultdict(collections.deque)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                dic[j+1].append(board[i][j])
    #stack
    stack = []

    for m in moves:
        next = 0
        if dic[m]:
            next = dic[m].popleft()
            if stack and stack[-1] == next:
                stack.pop()
                answer += 2
            else:
                stack.append(next)
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)
