import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(list(map(list, zip(temp, temp))))
# min, max
for i in range(1, N):
    arr[i][0][0] += min(arr[i-1][0][0], arr[i-1][1][0])
    arr[i][1][0] += min(arr[i-1][0][0], arr[i-1][1][0], arr[i-1][2][0])
    arr[i][2][0] += min(arr[i-1][1][0], arr[i-1][2][0])

    arr[i][0][1] += max(arr[i-1][0][1], arr[i-1][1][1])
    arr[i][1][1] += max(arr[i-1][0][1], arr[i-1][1][1], arr[i-1][2][1])
    arr[i][2][1] += max(arr[i-1][1][1], arr[i-1][2][1])

print(max(arr[-1], key = lambda x: x[1])[1], min(arr[-1], key=lambda x: x[0])[0], sep = ' ')


# import sys
# read = sys.stdin.readline
# arr = []
 
# N = int(read())
# maxD = [[0 for _ in range(3)] for _ in range(2)]
# minD = [[0 for _ in range(3)] for _ in range(2)]
# for i in range(N):
#     temp = list(map(int, read().split()))
 
#     maxD[1][0] = max(maxD[0][0], maxD[0][1]) + temp[0]
#     minD[1][0] = min(minD[0][0], minD[0][1]) + temp[0]
 
#     maxD[1][1] = max(maxD[0][0], maxD[0][1], maxD[0][2]) + temp[1]
#     minD[1][1] = min(minD[0][0], minD[0][1], minD[0][2]) + temp[1]
 
#     maxD[1][2] = max(maxD[0][1], maxD[0][2]) + temp[2]
#     minD[1][2] = min(minD[0][1], minD[0][2]) + temp[2]
 
#     maxD[0][0], maxD[0][1], maxD[0][2] = maxD[1][0], maxD[1][1], maxD[1][2]
#     minD[0][0], minD[0][1], minD[0][2] = minD[1][0], minD[1][1], minD[1][2]
 
# print(max(maxD[1]), min(minD[1]))
