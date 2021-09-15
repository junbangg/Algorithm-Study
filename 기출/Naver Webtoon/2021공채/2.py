#NASH 게임이론
#        B        B
#  A   2, 4    -5, -3
#  A   -10, 9   3, 6


def solution(matrix):
    # A1, A2, A3..일때 B 가 할 수 있는 최선의 선택
    B = [0] * len(matrix)
    A = [0] * len(matrix)
    for x in range(len(matrix)):
        bestChoice = len(matrix)
        maxWeight = -float('inf')
        for y in range(len(matrix)):
            _, b = matrix[x][y].split()
            if maxWeight < int(b):
                bestChoice = y
                maxWeight = int(b)
        
        A[x] = bestChoice
    for y in range(len(matrix)):
        bestChoice = len(matrix)
        maxWeight = -float('inf')
        for x in range(len(matrix)):
            a, _ = matrix[x][y].split()
            if maxWeight < int(a):
                bestChoice = x
                maxWeight = int(a)
        
        B[y] = bestChoice
    print(A)
    print(B)
    answer = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            answer += 1
    return answer

tc = [["2 4", "-5 -3"], ["-10 9", "3 6"]]
tc2 = [["5 4", "5 5"], ["5 5", "5 5"]]
print(solution(tc2))
            


        
