def solution(arr):
    def divide(row_s, row_e, col_s, col_e):
        #base case
        if row_e - row_s == 1 and col_e - col_s == 1:
            if arr[row_s][col_s] == 1:
                ones.append(1)
            else:
                zeros.append(0)
            return
        zero_one = arr[row_s][col_s]
        divide_switch = False
        for i in range(row_s+1, row_e):
            for j in range(col_s, col_e):
                if arr[i][j] != zero_one:
                    divide_switch = True
        if divide_switch:
            # top left
            divide(row_s, row_e/2, col_s, col_e/2)
            # top right
            divide(row_s + row_e/2, row_e/2, col_s, col_e/2)
            # bottom left
            divide(row_s, row_e/2, col_s + col_e/2, col_e/2)
            # bottom right
            divide(row_s + row_e/2, row_e/2, col_s + col_e/2, col_e/2)
        else:
            if zero_one == 0: zeros.append(0)
            else: ones.append(1)
            return
    ones = []
    zeros = []
    divide(0, len(arr), 0, len(arr[0]))
    return [len(zeros), len(ones)]


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))
