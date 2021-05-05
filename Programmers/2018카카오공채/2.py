def solution(n, arr1, arr2):
    answer= []
    for i in range(n):
        a = bin(arr1[i])[2:].zfill(n)
        b = bin(arr2[i])[2:].zfill(n)
        row = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                row += '#'
            else:
                row += ' '
        answer.append(row)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
