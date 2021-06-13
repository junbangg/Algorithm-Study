N, X, Y = map(int, input().split(' '))
result = 0
def navigate(n, x, y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y + 1 == Y:
            print(result)
            return
        result += 1
        return
    navigate(n//2, x, y)
    navigate(n//2, x, y + n // 2)
    navigate(n//2, x + n // 2, y)
    navigate(n//2, x + n//2, y + n // 2)
navigate(2 ** N, 0, 0)