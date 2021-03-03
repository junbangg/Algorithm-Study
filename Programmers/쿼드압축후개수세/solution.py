def solution(arr):
    def divide(row, col, k):
        #base case
        if k == 1:
            if arr[row][col] == 0:
                zeros.append(0)
            else:
                ones.append(1)
            return

        zero_one = arr[row][col]
        divide_switch = False
        for i in range(row, row+k):
            for j in range(col, col+k):
                if arr[i][j] != zero_one:
                    divide_switch = True
                    break
        if divide_switch:
            # top left
            divide(row, col, k/2)
            # top right
            divide(row, col + k/2, k/2)
            # bottom left
            divide(row + k/2, col, k/2)
            # bottom right
            divide(row + k/2, col + k/2, k/2)
        else:
            if zero_one == 0: zeros.append(0)
            else: ones.append(1)
            return
    ones = []
    zeros = []
    divide(0, 0, len(arr))
    return [len(zeros), len(ones)]


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))
