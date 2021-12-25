import sys
input = sys.stdin.readline

arr = []
N = int(input())
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()

_min, _max = arr[0][0], arr[0][1]
answer = 0
for i in range(1, N):
    start, end = arr[i]
    if start >= _max:
        answer += _max - _min
        _min = start
        _max = end
    elif _max <= end:
        _max = end
        
answer += _max - _min
print(answer)
    