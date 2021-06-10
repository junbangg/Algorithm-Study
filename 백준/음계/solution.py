# dont need function in baekjoon
def solution(arr):
    ascending, descending = True, True
    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            descending = False
        else:
            ascending = False
    if ascending:
        print('ascending')
    elif descending:
        print('descending')
    else:
        print('mixed')

testCase = list(map(int, input().split()))
solution(testCase)

