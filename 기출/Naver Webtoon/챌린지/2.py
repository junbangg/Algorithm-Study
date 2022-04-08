from operator import truediv


def solution(n, clockwise):
    def moveDown(x, y, num):
        array[x][y] = num
        x += 1
        num += 1
        while isValid(x, y) and array[x][y] == 0:
            array[x][y] = num
            x += 1
            num += 1

    def moveUp(x, y, num):
        array[x][y] = num
        x -= 1
        num += 1
        while isValid(x, y) and array[x][y] == 0:
            array[x][y] = num
            x -= 1
            num += 1
        return num

    def moveLeft(x, y, num):
        array[x][y] = num
        y -= 1
        num += 1
        while isValid(x, y) and array[x][y] == 0:
            array[x][y] = num
            y -= 1
            num += 1

    def moveRight(x, y, num):
        array[x][y] = num
        y += 1
        num += 1
        while isValid(x, y) and array[x][y] == 0:
            array[x][y] = num
            y += 1
            num += 1

    def isValid(x, y):
        return 0 <= x < n and 0 <= y < n

    depth = (n + 1) // 2

    num = 1
    array = [[0 for _ in range(n)] for _ in range(n)]

    if clockwise:
        for i in range(depth):
            moveDown(i, n - 1 - i, num)
            moveLeft(n - 1 - i, n - 1 - i, num)
            moveRight(i, i, num)
            num = moveUp(i, n - 1 - i, num)
    else:
        for i in range(depth):
            moveDown(i, i, num)
            moveLeft(i, n - 1 - i, num)
            moveRight(i, n - 1 - i, num)
            num = moveUp(n - 1 - i, n - 1 - i, num)

    return array

n = 5
clockwise = True

# n = 6
# clockwise = False

# n = 9
# clockwise = False
        
print(solution(n, clockwise))




