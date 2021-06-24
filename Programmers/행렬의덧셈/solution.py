def solution(arr1, arr2):
    answer = []
    for x in range(len(arr1)):
        temp = []
        for y in range(len(arr1[0])):
            temp.append(arr1[x][y] + arr2[x][y])
        answer.append(temp)
    return answer

# one liner using zip()
def solution(arr1, arr2):
    return [[a+b for a, b in zip(arr1[i], arr2[i])] for i in range(len(arr1))]
