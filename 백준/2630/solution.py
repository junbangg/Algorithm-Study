N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
one, zero = 0, 0

def count(x, y, size):
    zeros, ones = 0, 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            if map[i][j] == 1:
                ones += 1
            else:
                zeros += 1
    if ones == 0:
        return 0
    elif zeros == 0:
        return 1
    else:
        return -1

def divide(x, y, size):
    global one
    global zero
    cnt = count(x, y, size)
    if cnt == 1:
        one += 1
        return
    elif cnt == 0:
        zero += 1
        return
    # Upper left
    divide(x, y, size//2)
    # Upper right
    divide(x, y + size // 2, size // 2)
    # Lower left
    divide(x + size // 2, y, size // 2)
    # Lower right
    divide(x+ size//2, y + size//2, size//2)

divide(0, 0, N)
print(zero)
print(one)
