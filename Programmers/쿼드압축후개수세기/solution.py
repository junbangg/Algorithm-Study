def solution(arr):
     def divide(row_s, row_e, col_s, col_e):
     def divide(row, col, k):
         #base case
         if row_e - row_s == 1 and col_e - col_s == 1:
             if arr[row_s][col_s] == 1:
                 ones.append(1)
             else:
         if k == 1:
             if arr[row][col] == 0:
                 zeros.append(0)
             else:
                 ones.append(1)
             return
         zero_one = arr[row_s][col_s]

         zero_one = arr[row][col]
         divide_switch = False
         for i in range(row_s+1, row_e):
             for j in range(col_s, col_e):
         for i in range(row, row+k):
             for j in range(col, col+k):
                 if arr[i][j] != zero_one:
                     divide_switch = True
                     break
         if divide_switch:
             # top left
             divide(row_s, row_e/2, col_s, col_e/2)
             divide(row, col, k/2)
             # top right
             divide(row_s + row_e/2, row_e/2, col_s, col_e/2)
             divide(row, col + k/2, k/2)
             # bottom left
             divide(row_s, row_e/2, col_s + col_e/2, col_e/2)
             divide(row + k/2, col, k/2)
             # bottom right
             divide(row_s + row_e/2, row_e/2, col_s + col_e/2, col_e/2)
             divide(row + k/2, col + k/2, k/2)
         else:
             if zero_one == 0: zeros.append(0)
             else: ones.append(1)
             return
     ones = []
     zeros = []
     divide(0, len(arr), 0, len(arr[0]))
     divide(0, 0, len(arr))
     return [len(zeros), len(ones)]
