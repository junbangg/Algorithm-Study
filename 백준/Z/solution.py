N, X, Y = map(int, input().split(' '))
edge = 2 ** N
def navigate(x, y, count):
    if x == X and y == Y:
        return count
    if x < edge and y < edge:
        dir = count % 4
        if dir == 1 or dir == 3:
            # right
            return navigate(x, y+1, count+1)
        if dir == 2:
            #dl
            return navigate(x+1, y-1, count+1)
        if dir == 0:
            if y+1 == edge:
                # big left
                return navigate(x+1, 0, count+1)
            else:
                return navigate(x-1, y+1, count+1)
answer = navigate(0, 0, 1)
print(answer-1)