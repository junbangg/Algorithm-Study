import sys
N = int(sys.stdin.readline())
grid = [list(sys.stdin.readline())[:-1] for _ in range(N)]

def count(x, y, size):
    ones, zeros = 0, 0
    for i in range(x, x+size):
        for j in range(y, y+size):
            if grid[i][j] == '1':
                ones += 1
            else:
                zeros += 1
    if ones == 0:
        return '0'
    elif zeros == 0:
        return '1'
    else:
        return '2'
def recurse(x, y, size):
    # base case
    cnt = count(x,y,size)
    if cnt == '1' or cnt == '0':
        return cnt
       return '0'
    encode = '('
    encode += recurse(x, y, size//2)
    encode += recurse(x, y+size//2, size//2)
    encode += recurse(x+size//2, y, size//2)
    encode += recurse(x+size//2, y+size//2, size//2)
    return encode + ')'

print(recurse(0, 0, N))
