import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(list(zip(temp, temp)))
print(arr)