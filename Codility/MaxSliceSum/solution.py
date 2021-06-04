def solution(A):
    maxNum, current = A[0], A[0]
    if current < 0:
        current = 0
    for num in A[1:]:
        nextNum = current + num
        maxNum = max(nextNum, maxNum)
        if nextNum < 0:
            current = 0
        else:
            current = nextNum
    return maxNum




tc = [3,2,-6,4,0]
#tc1 = [5,-4,9,0,3,-6,4]
print(solution(tc))

