# def solution(board, skill):
#     answer = 0
#     def alter(type, x1, y1, x2, y2, degree):
#         for x in range(x1, x2+1):
#             for y in range(y1, y2+1):
#                     if type == 1:
#                         board[x][y] -= degree
#                     else:
#                         board[x][y] += degree
#                     # if board[x][y] <= 0:
#                         # answer += 1
    
#     for type, r1, c1, r2, c2, degree in skill:
#         alter(type, r1, c1, r2, c2, degree)
    
#     for x in range(len(board)):
#         for y in range(len(board[0])):
#             if board[x][y] > 0:
#                 answer += 1

            
#     return answer
def solution(board, skill):
    count, last = 1, len(skill)
    def alter(type, x1, y1, x2, y2, degree, count):
        answer = 0
        for x in range(len(board)):
            for y in range(len(board[0])):
                if x1 <= x <= x2 and y1 <= y <= y2:
                    if type == 1:
                        board[x][y] -= degree
                    else:
                        board[x][y] += degree
                if count == last:
                    if board[x][y] > 0:
                        answer += 1
        # for x in range(x1, x2+1):
        #     for y in range(y1, y2+1):
        #             if type == 1:
        #                 board[x][y] -= degree
        #             else:
        #                 board[x][y] += degree
        #             if count == last:
        #                 if board[x][y] > 0:
        #                     answer += 1
        return answer
    
    answer = 0
    for type, r1, c1, r2, c2, degree in skill:
        answer = alter(type, r1, c1, r2, c2, degree, count)
        count += 1
    
    # for x in range(len(board)):
    #     for y in range(len(board[0])):
    #         if board[x][y] > 0:
    #             answer += 1

            
    return answer
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
# board = [[1,2,3],[4,5,6],[7,8,9]]
# skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
# print(solution(board, skill))

# [0, 0, 3, 4], - 4
# [2, 0, 2, 3], + 3
# [1, 0, 3, 1], + 2
# [0, 1, 3, 3], - 1

X = [-5, -3, 0, -3]
Y = [1, 0, -2, -2, -4]


for i in range(len(board)):
    board[i] = list(map(lambda x: x+X[i], board[i]))
board = list(map(list, zip(*board)))
for j in range(len(board)):
    board[j] = list(map(lambda y: y+Y[j], board[j]))
print(board)
# for j in range(len(board[0])):
#     for x in range(len(board)):
#         board[x][j] += Y[j]


