import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

minus = one = zero = 0

def conquer(x, y, size):
    num = grid[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if num != grid[i][j]:
                num = 2
                break
    return num

def divide(x, y, size):
    global minus, one, zero
    # conquer
    res = conquer(x, y, size)
    if res == -1:
        minus += 1
        return
    if res == 0:
        zero += 1
        return
    if res == 1:
        one += 1 
        return
    # divide
    divide(x, y, size//3)
    divide(x, y+size//3, size//3)
    divide(x, y+2*size//3, size//3)

    divide(x+size//3, y, size//3)
    divide(x+size//3, y+size//3, size//3)
    divide(x+size//3, y+2*size//3, size//3)

    divide(x+2*size//3, y, size//3)
    divide(x+2*size//3, y+size//3, size//3)
    divide(x+2*size//3, y+2*size//3, size//3)

divide(0, 0, N)
print(minus)
print(zero)
print(one)