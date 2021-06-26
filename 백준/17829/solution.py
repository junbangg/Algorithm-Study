N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

def checkSecond(x, y):
    four = []
    for i in range(x, x+2):
        for j in range(y, y+2):
            four.append(map[i][j])
    return sorted(four)[-2]

def divide(x, y, size):
    if size == 2:
        return checkSecond(x, y)
    four = []
    # upper left
    four.append(divide(x, y, size//2))
    # upper right
    four.append(divide(x, y + size//2, size//2))
    # lower left
    four.append(divide(x+size//2, y, size//2))
    # lower right
    four.append(divide(x+size//2, y + size//2, size//2))
    return sorted(four)[-2]

print(divide(0, 0, N))
