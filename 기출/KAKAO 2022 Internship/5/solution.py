def printBoard(board):
    for x in range(len(board)):
        print(*board[x])

# 회전 함수
def rotate(x1, y1, x2, y2, arr):
    # up -> left -> down -> right
    cache = arr[x1][y1]
        # up
    for row in range(x1 + 1, x2 + 1):
        arr[row - 1][y1] = arr[row][y1]
    # left
    for col in range(y1 + 1, y2 + 1):
        arr[x2][col-1] = arr[x2][col]
    # down
    for row in range(x2 - 1, x1 - 1, -1):
        arr[row + 1][y2] = arr[row][y2]
    # right
    for col in range(y2 - 1, y1 - 1, - 1):
        arr[x1][col + 1] = arr[x1][col]
    # cache
    arr[x1][y1 + 1] = cache

    return arr

def shift(rowCount, arr):
    newArr = [arr[rowCount-1]]
    for i in range(rowCount-1):
        newArr.append(arr[i])
    return newArr

def solution(rc, operations):
    rowLength = len(rc)
    colLength = len(rc[0])
    for operation in operations:
        if operation == "Rotate":
            rc = rotate(0, 0, rowLength-1, colLength-1, rc)
        else:
            rc = shift(rowLength, rc)
    return rc

# tc1
# rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# operations = ["Rotate", "ShiftRow"]
# tc2

# tc3
rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
printBoard(solution(rc, operations))