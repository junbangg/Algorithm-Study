tc = int(input())
for _ in range(tc):
    M, N, tx, ty = map(int, input().split())
    x = y = 1
    count = 1
    answer = -1
    for i in range(40001):
        if x == tx and y == ty:
            answer = count
            break
        if x < M: x += 1
        else: x = 1
        if y < N: y += 1
        else: y = 1
        count += 1
    print(answer)